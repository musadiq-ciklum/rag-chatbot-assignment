# RAG Chatbot — Assignment 04

This project is part of a step-by-step implementation of a **Retrieval-Augmented Generation (RAG)** system.  
The first completed module is **PDF Processing**, which extracts structured and cleaned text from lecture slides so it can later be used for chunking, embeddings, vector search, and chatbot responses.

---

## 📦 Installation & Setup

### 1. Clone the Repository

**SSH**
```bash
git clone git@github.com:musadiq-ciklum/rag-chatbot-assignment.git
```

**HTTPS**
```bash
git clone https://github.com/musadiq-ciklum/rag-chatbot-assignment.git
```

**Navigate into the folder:**
```bash
cd rag-chatbot-assignment
```

**Install Requirements**
```bash
pip install -r requirements.txt
```

**Run Project Setup**
```bash
python tools/setup_project.py
```

**Run The Tests**
```bash
python pytest tests/
```