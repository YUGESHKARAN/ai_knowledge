# 📚 AI Knowledge Feed Pipeline


## 📝 Overview

**AI Knowledge** is the knowledge ingestion and embedding pipeline for your AI projects. This repository enables users to upload, preprocess, and embed documents, then store them as high-dimensional vectors in a Pinecone vector database. These embeddings can then be leveraged by conversational AI systems (such as [pinecone_ai](https://github.com/YUGESHKARAN/pinecone_ai)) to answer domain-specific questions with up-to-date, relevant information—without the need for model fine-tuning or retraining.

## ✨ Features

- 📥 **Document Ingestion**: Upload one or more documents for processing.
- 🧬 **Embedding Generation**: Convert documents into 384-dimensional semantic embeddings.
- 🌲 **Pinecone Integration**: Seamlessly store embeddings in your Pinecone vector database for scalable, real-time search.
- 🔗 **Plug-and-Play for Chatbots**: Use this knowledge feed with conversational AI systems to boost their domain expertise.
- ⚡ **Lightweight & Fast**: Minimal dependencies and quick setup for immediate use.

## 🚀 Getting Started

### ✅ Prerequisites

- 🐍 Python 3.8+
- Pinecone account and API key
- Hugging Face account and API key

### 🔐 Required Environment Variables

Create a `.env` file in the root directory and add the following keys:
```env
HUGGINGFACE_API_KEY=your_huggingface_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

### 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YUGESHKARAN/ai_knowledge.git
   cd ai_knowledge
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables:**
   - Set your Hugging Face and Pinecone API keys as described above.

### ▶️ Running the Pipeline

```bash
python index.py
```

## 🗂️ Project Structure

- `index.py`: Main application file for document upload, embedding, and Pinecone storage.
- `requirements.txt`: Python dependencies.
- `.gitignore`: Git ignored files.

## ⚙️ How It Works

1. **Upload Documents**: Add your knowledge sources (PDFs, text files, etc.).
2. **Embedding**: Each document is processed and converted into a 384-dimensional embedding vector using Hugging Face models.
3. **Pinecone Storage**: Embeddings are pushed to your Pinecone vector database for efficient retrieval.
4. **AI Consumption**: Your conversational AI can now access this knowledge and provide domain-specific answers.

> For a ready-to-use chatbot leveraging this pipeline, see [pinecone_ai](https://github.com/YUGESHKARAN/pinecone_ai).

## 🛠️ Technologies Used

- 🐍 Python
- 🌲 Pinecone Vector Database
- 🤗 Hugging Face

## 🤝 Contributing

Contributions are welcome! Open an issue or submit a pull request for improvements or bug fixes.

## 📄 License

This project is licensed under the MIT License.

## 📬 Contact

For questions or support, Contact [YUGESHKARAN](https://github.com/YUGESHKARAN).

---
