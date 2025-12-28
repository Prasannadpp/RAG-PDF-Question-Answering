A console-based Retrieval-Augmented Generation (RAG) application that answers questions based on the content of PDF files.
It uses LangChain, ChromaDB, and Groq-hosted LLMs to perform semantic search and generate accurate, context-aware answers./



✨ Features: /
Upload and process PDF files/
Semantic search using vector embeddings/
Answers grounded strictly in PDF content/
Handles large PDFs efficiently with chunking/
Clean console-based interaction/
Prevents hallucinated answers/
Secure API key handling via environment variables



🛠️ Tech Stack: /
Python/
LangChain/
ChromaDB/
Groq (LLM inference)/
HuggingFace Sentence Transformers/
PyPDF2


📁 Project Structure
```
rag-project/
│
├── RAG_APPLICATION.py   # Main application
├── requirements.txt     # Dependencies
├── README.md            # Documentation
├── .env.example         # API key template
├── .gitignore
└── venv/                # Virtual environment (not committed)
```

🚀 Setup & Installation
1. Clone the repository: 

git clone https://github.com/<your-username>/rag-project.git
cd rag-project

2. Create and activate virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Set up environment variables: Create a .env file:

GROQ_API_KEY=your_groq_api_key_here


▶️ Running the Application/
TOKENIZERS_PARALLELISM=false venv/bin/python RAG_APPLICATION.py

How it works:/
Select a PDF file when prompted/
The PDF is indexed using vector embeddings/
Ask questions in the terminal/
The system retrieves relevant content and generates answers/
Type exit to quit

🧪 Example Queries: /
Summarize the PDF/
What are the key points of the document?/
If an answer is not found in the PDF, the system responds:/
Not found in the PDF.

📦 Dependencies:

langchain/
langchain-community/
langchain-groq/
langchain-huggingface/
chromadb/
PyPDF2/
sentence-transformers/
python-dotenv


🔒 Notes/
API keys are never committed to GitHub/
The application only answers based on document content/
Designed to handle large PDFs without exceeding token limits
