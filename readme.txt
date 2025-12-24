This project implements a console-based Retrieval-Augmented Generation (RAG) system using LangChain, ChromaDB, and Groq for answering user queries based on uploaded PDF files. The application is designed to extract text, perform vector-based semantic search, and generate answers using a hosted language model.

All code is implemented in a Google Colab notebook.

Files that are included:
RAG_APPLICATION_R11933956.ipynb :  The main Colab notebook containing the complete implementation.
README.txt        		: This instruction file.
requirements.txt  		: List of required Python libraries.

Instructions to run the Project:

Step1: In Google Colab, open the RAG_APPLICATION_R11933956.ipynb notebook.
Step2: Install dependencies: pip install -r requirements.txt (if required ) As all the required are already installed in the notebook
Step3: Follow the step-by-step directions included in the notebook.
Step4: Upload one or more PDF files when prompted.
Step5: Ask questions in the input cell provided.
Step6: The system will use the Groq LLM to produce replies and ChromaDB to access relevant information.  

requirements.txt: 

langchain 		: for managing document loading and retrieval
langchain-community	: Provides ChromaDB and other integrations not in the core LangChain.
langchain-groq		: for LLM-based question answering
langchain-huggingface	: for loading HuggingFace sentence transformers for text embeddings.
chromadb		: for vector indexing and similarity search
PyPDF2			: for extracting text from PDFs
sentence-transformers	: for generating semantic embeddings from document chunks for retrieval.

Test Cases  
Example queries (tested in notebook):  (screenshots are also attached in the ZIP file for reference)
1. explain the grading criteria
2. summarise the whole pdf information
3. what is written by suraj bansal
4. what are the keypoints of the pdf

Sample pdf that is used for testing is also attached in the ZIP file