# 📄 AI Long Text Summarizer

A Streamlit-powered AI application that summarizes long text documents using LangChain's Map-Reduce summarization chain and Groq-hosted LLMs.

## 🚀 Overview

Large Language Models often struggle with very long documents due to context window limitations. This application solves that problem by splitting large text files into smaller chunks, summarizing each chunk individually, and then combining the results into a concise final summary.

The application provides a simple web interface where users can:

* Upload a `.txt` document
* Enter their Groq API Key
* Generate AI-powered summaries
* Process documents larger than a single prompt context

---

## ✨ Features

* 📂 Upload text files (`.txt`)
* ✂️ Automatic document chunking
* 🔄 LangChain Map-Reduce summarization
* 🤖 Groq LLM integration
* 🌐 Simple Streamlit UI
* 📜 Handles long documents efficiently
* ⚡ Fast inference using Groq API

---

## 🛠️ Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* OpenAI-Compatible API Interface
* RecursiveCharacterTextSplitter

---

## 📁 Project Structure

```text
004-Long-Text-Summarizer/
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env
├── README.md
│
└── sample_files/
    └── roman_history_test.txt
```

---

## ⚙️ How It Works

### Step 1: Upload Document

The user uploads a `.txt` file.

### Step 2: Text Processing

The uploaded document is converted into plain text.

### Step 3: Document Chunking

LangChain's RecursiveCharacterTextSplitter breaks the document into manageable chunks.

```python
chunk_size = 5000
chunk_overlap = 350
```

### Step 4: Map Phase

Each chunk is independently summarized by the LLM.

### Step 5: Reduce Phase

All chunk summaries are combined into one final summary.

### Step 6: Display Result

The final summary is shown in the Streamlit application.

---

## 🧠 Summarization Workflow

```text
Upload File
     │
     ▼
Read Text
     │
     ▼
Split Into Chunks
     │
     ▼
Map Summaries
     │
     ▼
Combine Summaries
     │
     ▼
Final Summary
```

---

## 📦 Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd 004-Long-Text-Summarizer
```

### Create Virtual Environment

Using Poetry:

```bash
poetry install
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 API Key

Generate a Groq API Key from:

https://console.groq.com/keys

Enter the key in the application when prompted.

---

## ▶️ Run Application

```bash
streamlit run main.py
```

The application will start on:

```text
http://localhost:8501
```

---

## 📄 Sample Test File

A sample text file is included for testing:

```text
sample_files/
└── roman_history_test.txt
```

This file contains a short history of Ancient Rome and can be used to verify summarization functionality.

---

## 📋 requirements.txt

```txt
streamlit
langchain
langchain-openai
openai
tiktoken
```

---

## 🚫 .gitignore

```gitignore
# Environment
.env

# Python
__pycache__/
*.pyc
*.pyo

# Streamlit
.streamlit/

# Virtual Environments
.venv/
venv/

# IDE
.vscode/
.idea/

# Jupyter
.ipynb_checkpoints/

# OS Files
.DS_Store
Thumbs.db
```

---

## 🔮 Future Improvements

* Support PDF documents
* Support DOCX files
* Download summary as TXT/PDF
* Adjustable summary length
* Multi-model support
* Batch document summarization
* Summary history tracking

---

## 👨‍💻 Author

**Ayush Pandey**

Building AI-powered applications using Python, LangChain, Streamlit, and LLM technologies.
