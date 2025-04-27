# 📚 College FAQ Bot using Gemini, LangChain, HuggingFace & FAISS

An intelligent FAQ bot that answers college-related questions using real data stored locally.  
Built with **Gemini-Pro**, **LangChain**, **Hugging Face embeddings**, and **FAISS**.

---

## ✨ Technologies Used

| Technology | Purpose |
|:-----------|:--------|
| [Google Gemini-Pro](https://ai.google.dev/) | LLM for answering questions |
| [LangChain](https://www.langchain.dev/) | Framework to create LLM pipelines |
| [Hugging Face Sentence Transformers](https://www.sbert.net/) | Generate semantic embeddings |
| [FAISS](https://github.com/facebookresearch/faiss) | Fast vector similarity search |
| [Python](https://www.python.org/) | Core language |
| [dotenv](https://pypi.org/project/python-dotenv/) | Manage environment variables |

---

## 🛠️ How the Project Works

1. **Data Loading**  
   Loads a CSV file `college_questions_answers.csv` containing Questions and Answers.

2. **Embeddings Generation**  
   Uses **HuggingFace's all-MiniLM-L6-v2** model to embed questions into dense vector representations.

3. **Vector Database Creation**  
   Stores vectors into a **FAISS** index locally for efficient semantic search.

4. **Retrieval**  
   Retrieves the most similar questions from FAISS based on vector similarity.

5. **Answer Generation**  
   Uses **Gemini-Pro** LLM to generate answers based strictly on retrieved context.

6. **Chain Architecture**  
   Combines retrieval and generation using **LangChain's RetrievalQA Chain**.

---

## 📋 Project Structure

```bash
.
├── college_questions_answers.csv  # Dataset with Q&A
├── faiss_index/                   # FAISS Index (auto-created after first run)
├── .env                            # API Key for Google Gemini
├── main.py                         # Main logic (Gemini, LangChain, FAISS)
├── README.md                       # Project documentation
