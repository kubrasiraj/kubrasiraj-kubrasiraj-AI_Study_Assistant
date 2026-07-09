"""
AI Study Assistant - Streamlit Frontend

This module provides a professional web interface for the AI Study Assistant.
It integrates with the existing backend RAG pipeline without modifying any
existing code.

The UI connects to the backend through:
- rag.rag_pipeline.initialize_rag(file_path) -> retriever
- models.llm.create_llm() -> model
- chat.chat.ask_question(question, mode, retriever, model) -> answer
"""

import os
import tempfile
import streamlit as st
from pathlib import Path

# Import existing backend components
from rag.rag_pipeline import initialize_rag
from models.llm import create_llm
from chat.chat import ask_question

# Page configuration
st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional appearance
st.markdown("""
    <style>
        .main-header {
            font-size: 2.5rem;
            color: #1E3A8A;
            text-align: center;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.1rem;
            color: #4B5563;
            text-align: center;
            margin-bottom: 2rem;
        }
        .chat-container {
            background-color: #FFFFFF;
            border-radius: 0.5rem;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }
        .user-message {
            background-color: #EFF6FF;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            margin: 0.5rem 0;
            border-left: 4px solid #3B82F6;
        }
        .assistant-message {
            background-color: #F3F4F6;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
            margin: 0.5rem 0;
            border-left: 4px solid #10B981;
        }
        .sidebar-section {
            padding: 0.5rem 0;
        }
        .status-indicator {
            padding: 0.5rem;
            border-radius: 0.25rem;
            margin: 0.5rem 0;
        }
        .upload-section {
            border: 2px dashed #D1D5DB;
            border-radius: 0.5rem;
            padding: 1.5rem;
            text-align: center;
            margin: 1rem 0;
        }
        .stButton > button {
            width: 100%;
            margin-top: 0.5rem;
        }
        .mode-selector {
            margin: 1rem 0;
        }
        .footer {
            text-align: center;
            color: #9CA3AF;
            font-size: 0.8rem;
            margin-top: 2rem;
            padding: 1rem 0;
            border-top: 1px solid #E5E7EB;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
def initialize_session_state():
    """Initialize all session state variables needed for the application."""
    # Chat history storage
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # PDF processing status
    if "pdf_loaded" not in st.session_state:
        st.session_state.pdf_loaded = False
    
    # Store the retriever from initialize_rag()
    if "retriever" not in st.session_state:
        st.session_state.retriever = None
    
    # Store the LLM model from create_llm()
    if "model" not in st.session_state:
        st.session_state.model = None
    
    # Current learning mode
    if "mode" not in st.session_state:
        st.session_state.mode = "Student Mode"
    
    # Current PDF file path for reference
    if "pdf_path" not in st.session_state:
        st.session_state.pdf_path = None
    
    # Track if processing is in progress
    if "processing" not in st.session_state:
        st.session_state.processing = False

# Main application header
def display_header():
    """Display the application header with title and description."""
    st.markdown('<div class="main-header">📚 AI Study Assistant</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">'
        'Upload your PDF and ask questions with context-aware AI responses'
        '</div>',
        unsafe_allow_html=True
    )

# Sidebar with configuration and PDF upload
def setup_sidebar():
    """
    Setup the sidebar with all configuration options:
    - PDF upload
    - Learning mode selection
    - Application information
    - Status indicators
    """
    with st.sidebar:
        st.markdown("## ⚙️ Configuration")
        
        # Learning Mode Selection
        st.markdown("### 📖 Learning Mode")
        mode_options = ["Student Mode", "Easy Mode", "Exam Mode", "Interview Mode"]
        selected_mode = st.selectbox(
            "Select your learning mode",
            mode_options,
            index=mode_options.index(st.session_state.mode),
            help="Different modes provide responses tailored to specific learning needs"
        )
        st.session_state.mode = selected_mode
        
        # Display mode description
        mode_descriptions = {
            "Student Mode": "Detailed explanations suitable for students",
            "Easy Mode": "Simplified explanations for beginners",
            "Exam Mode": "Concise, exam-focused answers",
            "Interview Mode": "Technical answers for interview preparation"
        }
        st.info(f"💡 **{mode_descriptions[selected_mode]}**")
        
        st.divider()
        
        # PDF Upload Section
        st.markdown("### 📄 PDF Upload")
        st.markdown("Upload a PDF document to start asking questions")
        
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type="pdf",
            label_visibility="collapsed"
        )
        
        # Process uploaded PDF
        if uploaded_file is not None and not st.session_state.processing:
            with st.spinner("🔄 Processing PDF..."):
                try:
                    # Save uploaded file temporarily using tempfile
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        temp_path = tmp_file.name
                    
                    # Update session state
                    st.session_state.pdf_path = temp_path
                    st.session_state.processing = True
                    
                    # Initialize RAG pipeline using existing function
                    # This creates the vector store and returns a retriever
                    retriever = initialize_rag(temp_path)
                    st.session_state.retriever = retriever
                    
                    # Create LLM model using existing function
                    model = create_llm()
                    st.session_state.model = model
                    
                    # Update status
                    st.session_state.pdf_loaded = True
                    st.session_state.processing = False
                    
                    # Clear chat history when new PDF is loaded
                    st.session_state.messages = []
                    
                    st.success(f"✅ **{uploaded_file.name}** loaded successfully!")
                    st.toast("PDF processed and ready for questions", icon="✅")
                    
                except Exception as e:
                    st.session_state.processing = False
                    st.error(f"❌ Error loading PDF: {str(e)}")
                    st.session_state.pdf_loaded = False
        
        # Show current PDF status
        if st.session_state.pdf_loaded and st.session_state.pdf_path:
            st.markdown("---")
            st.markdown("### 📊 Document Status")
            st.markdown("✅ **PDF Loaded**")
            st.markdown(f"📄 File: `{Path(st.session_state.pdf_path).name}`")
            
            if st.button("🔄 Clear PDF & Reset", type="secondary"):
                # Clean up temporary file if it exists
                if st.session_state.pdf_path and os.path.exists(st.session_state.pdf_path):
                    try:
                        os.unlink(st.session_state.pdf_path)
                    except:
                        pass
                
                # Reset session state
                st.session_state.pdf_loaded = False
                st.session_state.pdf_path = None
                st.session_state.retriever = None
                st.session_state.model = None
                st.session_state.messages = []
                st.rerun()
        
        st.divider()
        
        # Application Information
        st.markdown("### ℹ️ About")
        st.markdown("""
        **AI Study Assistant** uses Retrieval-Augmented Generation (RAG)
        to answer questions based on your uploaded PDF documents.
        
        **How it works:**
        1. Upload a PDF document
        2. Select a learning mode
        3. Ask questions about the content
        4. Get AI-generated answers with context
        """)
        
        st.divider()
        
        # Statistics
        if st.session_state.pdf_loaded:
            st.markdown("### 📈 Session Stats")
            st.markdown(f"- **Mode:** {st.session_state.mode}")
            st.markdown(f"- **Questions:** {len(st.session_state.messages) // 2}")
            st.markdown("- **Status:** Ready for questions")
        else:
            st.warning("⚠️ No PDF loaded")

# Display chat messages in a chat-style interface
def display_chat_messages():
    """
    Display all chat messages from session state.
    Uses st.chat_message for proper chat interface.
    """
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Handle user input and generate response
def handle_user_input(prompt: str):
    """
    Process user question using the existing ask_question function.
    
    The function uses:
    - st.session_state.retriever (from initialize_rag)
    - st.session_state.model (from create_llm)
    - st.session_state.mode (selected by user)
    
    Args:
        prompt: User's question
    """
    if not prompt.strip():
        return
    
    # Check if PDF is loaded
    if not st.session_state.pdf_loaded or st.session_state.retriever is None:
        with st.chat_message("assistant"):
            st.warning("⚠️ Please upload a PDF document first before asking questions.")
        return
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response using existing backend function
    with st.chat_message("assistant"):
        with st.spinner("🧠 Generating answer..."):
            try:
                # Call the existing ask_question function with all required parameters
                answer = ask_question(
                    question=prompt,
                    mode=st.session_state.mode,
                    retriever=st.session_state.retriever,
                    model=st.session_state.model
                )
                
                # Display the answer
                st.markdown(answer)
                
                # Add assistant message to chat history
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except Exception as e:
                error_msg = f"❌ Error generating answer: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Main application flow
def main():
    """
    Main application entry point.
    Handles the overall layout and flow of the Streamlit app.
    """
    # Initialize session state
    initialize_session_state()
    
    # Setup sidebar
    setup_sidebar()
    
    # Main content area
    display_header()
    
    # Create a container for chat messages with custom styling
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    # Display chat messages
    display_chat_messages()
    
    # Add a divider for visual separation
    st.divider()
    
    # Chat input at the bottom
    prompt = st.chat_input(
        "Ask a question about your document...",
        disabled=not st.session_state.pdf_loaded
    )
    
    if prompt:
        handle_user_input(prompt)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown(
        '<div class="footer">'
        'AI Study Assistant v1.0 | Built with Streamlit & RAG | Powered by Mistral AI'
        '</div>',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()