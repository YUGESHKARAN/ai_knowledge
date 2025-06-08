import os
import uuid
from flask import Flask, request, jsonify
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import pinecone
from io import BytesIO
from PyPDF2 import PdfReader

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Initialize Pinecone
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
INDEX_NAME = "ai-knowledge-feed"

# Embedding & text splitter
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)

# In-memory PDF upload route
@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        # Read PDF in-memory
        pdf_bytes = BytesIO(file.read())
        reader = PdfReader(pdf_bytes)

        # Combine all text
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

        # Split into chunks
        chunks = text_splitter.split_text(text)

        # Create index if not exists
        if INDEX_NAME not in pc.list_indexes().names():
            pc.create_index(name=INDEX_NAME, dimension=embeddings.embedding_dimension)
        pinecone_index = pc.Index(INDEX_NAME)

        # Insert embeddings
        for i, chunk in enumerate(chunks):
            embedding = embeddings.embed_query(chunk)
            uid = str(uuid.uuid4())
            pinecone_index.upsert([(uid, embedding, {"text": chunk})])

        return jsonify({"message": "PDF processed in-memory and vectorized successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4500))
    app.run(port=port, debug=True)
