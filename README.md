# AI Study Assistant

AI Study Assistant is a modular Retrieval-Augmented Generation (RAG) application that allows users to ask questions from their own PDF documents.

The project retrieves the most relevant content from the uploaded PDF and uses a Large Language Model (Mistral AI) to generate answers based only on the retrieved context.

This project was built as part of my AI Engineering learning journey to understand how modern RAG applications are designed and implemented.

---

## Features

- Ask questions from any uploaded PDF
- Multiple response modes:
  - Student Mode
  - Easy Mode
  - Exam Mode
  - Interview Mode
- Modular project structure
- FAISS vector database
- HuggingFace sentence embeddings
- Mistral AI integration
- Prompt engineering for different learning styles

---

## Project Structure

```
AI_STUDY_ASSISTANT/

├── chat/
├── data/
├── models/
├── prompts/
├── rag/
├── utils/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Technologies Used

- Python
- LangChain
- Mistral AI
- HuggingFace Embeddings
- FAISS
- PyPDF
- Python Dotenv

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd AI_STUDY_ASSISTANT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Mistral API key.

```text
MISTRAL_API_KEY=your_api_key
```

Run the project

```bash
python app.py
```

---

## How It Works

1. Load the PDF
2. Split the document into chunks
3. Create embeddings
4. Store embeddings in FAISS
5. Retrieve the most relevant chunks
6. Generate an answer using Mistral AI
7. Display the response according to the selected mode

---

## Current Status

Backend development is complete.

The next step is to build a Streamlit user interface for a better user experience.

---

## Future Improvements

- Streamlit UI
- Chat history
- Conversation memory
- Multiple PDF support
- Citation support
- Source highlighting

---

## Author

Kubra Siraj
# AI Study Assistant

AI Study Assistant is a modular Retrieval-Augmented Generation (RAG) application that allows users to ask questions from their own PDF documents.

The project retrieves the most relevant content from the uploaded PDF and uses a Large Language Model (Mistral AI) to generate answers based only on the retrieved context.

This project was built as part of my AI Engineering learning journey to understand how modern RAG applications are designed and implemented.

---

## Features

- Ask questions from any uploaded PDF
- Multiple response modes:
  - Student Mode
  - Easy Mode
  - Exam Mode
  - Interview Mode
- Modular project structure
- FAISS vector database
- HuggingFace sentence embeddings
- Mistral AI integration
- Prompt engineering for different learning styles

---

## Project Structure

```
AI_STUDY_ASSISTANT/

├── chat/
├── data/
├── models/
├── prompts/
├── rag/
├── utils/
├── app.py
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Technologies Used

- Python
- LangChain
- Mistral AI
- HuggingFace Embeddings
- FAISS
- PyPDF
- Python Dotenv

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder

```bash
cd AI_STUDY_ASSISTANT
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Mistral API key.

```text
MISTRAL_API_KEY=your_api_key
```

Run the project

```bash
python app.py
```

---

## How It Works

1. Load the PDF
2. Split the document into chunks
3. Create embeddings
4. Store embeddings in FAISS
5. Retrieve the most relevant chunks
6. Generate an answer using Mistral AI
7. Display the response according to the selected mode

---

## Current Status

Backend development is complete.

The next step is to build a Streamlit user interface for a better user experience.

---

## Future Improvements

- Streamlit UI
- Chat history
- Conversation memory
- Multiple PDF support
- Citation support
- Source highlighting

---


## Author

**Kubra Siraj**

Aspiring AI Engineer

Currently learning:
- Python
- FastAPI
- LangChain
- RAG
- Agentic AI