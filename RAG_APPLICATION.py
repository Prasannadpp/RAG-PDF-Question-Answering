import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog

from dotenv import load_dotenv
load_dotenv()

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
print("RUNNING FILE:", __file__)

# ---------- Pick PDF ----------
root = tk.Tk()
root.withdraw()

pdf_path = filedialog.askopenfilename(
    title="Select a PDF file",
    filetypes=[("PDF files", "*.pdf")]
)
if not pdf_path:
    raise ValueError("No PDF file selected.")


# ---------- Extract text ----------
reader = PdfReader(pdf_path)
text = ""
for page in reader.pages:
    content = page.extract_text()
    if content:
        text += content + "\n"

print("✅ Text extracted successfully.")
print("Total characters extracted:", len(text))


# ---------- Chunk ----------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    separators=["\n\n", "\n", " ", ""]
)
text_chunks = splitter.split_text(text)
print("✅ Text split into", len(text_chunks), "chunks.")


# ---------- Vector store ----------
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_texts(text_chunks, embedding=embedding_model)
print("✅ Vector store created.")


# ---------- Groq LLM ----------
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("Missing GROQ_API_KEY. Put it in a .env file as GROQ_API_KEY=...")

llm = ChatGroq(
    api_key=groq_api_key,
    model_name="llama-3.1-8b-instant",
    temperature=0,   # more faithful / less creative
)
print("✅ LLM initialized using Groq.")


# ---------- Retriever ----------
retriever = vectorstore.as_retriever(search_kwargs={"k": 10})
print("✅ Retriever is ready.")


def answer_query(user_query: str) -> str:
    docs = retriever.invoke(user_query)
    context = "\n\n".join(d.page_content for d in docs).strip()

    if not context:
        return "Not found in the PDF."

    prompt = (
        "You are answering questions about a PDF.\n"
        "CRITICAL RULES:\n"
        "1) Use ONLY the CONTEXT. Do NOT use outside knowledge.\n"
        "2) If the answer is not explicitly in the CONTEXT, reply exactly: Not found in the PDF.\n"
        "3) Do NOT add tutorials, steps, code, links, or recommendations.\n"
        "4) Provide the answer, then include 1-3 short supporting quotes from the CONTEXT.\n\n"
        f"CONTEXT:\n{context}\n\n"
        f"QUESTION: {user_query}\n"
        "ANSWER:"
    )

    resp = llm.invoke(prompt)
    out = getattr(resp, "content", str(resp)).strip()

    # Cut off any weird artifacts if the model emits them
    for marker in ["<|end_header_id|>", "assistant<|", "1assistant<|"]:
        if marker in out:
            out = out.split(marker, 1)[0].strip()

    return out


while True:
    query = input("\nAsk a question (or type 'exit'): ").strip()

    # Ensure exit never reaches the model (handles "exit " too)
    if query.lower() == "exit":
        print("\nExiting. Thank you!")
        break

    try:
        answer = answer_query(query)
        print("\nAnswer:", answer)
    except Exception as e:
        print("\nError during query:", e)
