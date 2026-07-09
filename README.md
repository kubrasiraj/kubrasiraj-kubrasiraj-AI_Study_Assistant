#  AI Study Assistant

AI Study Assistant is a PDF-based Retrieval-Augmented Generation (RAG) application that helps students learn from their own study material.

Users can upload a PDF document and ask questions related to its content. The application retrieves relevant information from the document and generates answers using an LLM while keeping responses focused on the provided context.

This project was built to understand how modern Generative AI applications work, including document processing, embeddings, vector search, retrieval pipelines, and LLM-based response generation.

---

##  Features

- Upload and chat with PDF documents
- Ask questions from your own study material
- Context-based answers using RAG pipeline
- Multiple learning modes:

  - **Student Mode**  
    Provides detailed explanations like a teacher.

  - **Easy Mode**  
    Explains concepts in simple beginner-friendly language.

  - **Exam Mode**  
    Generates concise and exam-focused answers.

- PDF text extraction and processing
- Document chunking for better retrieval
- Semantic search using vector embeddings
- FAISS vector database integration
- Mistral AI integration for response generation
- Streamlit-based interactive interface
- Custom prompt engineering for different learning styles

---

##  How It Works

The application follows a Retrieval-Augmented Generation workflow:

```
User uploads PDF
        |
        ↓
Extract text from document
        |
        ↓
Split document into smaller chunks
        |
        ↓
Generate embeddings using HuggingFace model
        |
        ↓
Store embeddings in FAISS vector database
        |
        ↓
Retrieve relevant information for user query
        |
        ↓
Generate response using Mistral AI
        |
        ↓
Display answer according to selected mode
```

---

##  Project Structure

```
AI_STUDY_ASSISTANT/

│
├── chat/
│   └── Question answering logic
│
├── models/
│   └── LLM configuration
│
├── prompts/
│   ├── student_prompt.py
│   ├── easy_prompt.py
│   └── exam_prompt.py
│
├── rag/
│   ├── loader.py
│   ├── splitter.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   ├── retriever.py
│   └── rag_pipeline.py
│
├── app.py
├── requirements.txt
├── .env.example
└── README.md
```

---

##  Technologies Used

**Programming Language**
- Python

**Generative AI**
- LangChain
- Mistral AI

**RAG Components**
- HuggingFace Sentence Transformers
- FAISS Vector Database
- PyPDF

**Frontend**
- Streamlit

**Environment**
- Python-dotenv

---

##  Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project directory

```bash
cd AI_STUDY_ASSISTANT
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Add environment variables

Create a `.env` file and add your Mistral API key:

```env
MISTRAL_API_KEY=your_api_key
```

### Run the application

```bash
streamlit run app.py
```

---

## 📖 Usage

1. Open the application.

2. Upload a PDF document.

3. Select a learning mode:

### Student Mode
For detailed explanations and understanding concepts.

### Easy Mode
For simple explanations suitable for beginners.

### Exam Mode
For short and focused exam preparation.

4. Ask questions from the uploaded document.

Example:

```
Explain supervised learning
```

The system retrieves relevant information from the PDF and generates an answer based on the selected mode.

---

##  What I Learned

While building this project, I explored:

- Building a complete RAG pipeline
- Working with document loaders and text splitters
- Creating and using embeddings
- Vector database concepts
- Retrieval-based question answering
- Prompt engineering
- LLM integration with LangChain
- Building AI applications using Streamlit

---

## 🔮 Future Improvements

- Chat history and memory
- Support for multiple PDF documents
- Source references in answers
- Highlighting relevant document sections
- Better document management

---

## Author

**Kubra Siraj**

Aspiring AI Engineer

Currently learning:

- Generative AI
- RAG Applications
- LangChain
- FastAPI
- Agentic AI
- LLM Applications