Core Purpose:

A persistent RAG (Retrieval-Augmented Generation) system that answers questions about your documents using local AI models with guaranteed database persistence.

This repository contains two ways to run the RAG application:
1. A unified Streamlit application (`app.py`) that allows you to choose your data source from a UI menu.
2. Separate command-line scripts for each data source (`ragtotext.py`, `ragtodb.py`, `ragtosqlite.py`).

## Running with Docker

### Build the Docker Image
```bash
docker build -t rag-app .
```

### Run the Unified Application
This is the default command for the Docker container. It will start a web server on port 8501.
```bash
docker run -p 8501:8501 rag-app
```
Open your browser and navigate to `http://localhost:8501`. Use the sidebar to select the data source you want to chat with.

### Run the Separate Scripts

#### 1. Run the Text File RAG Script (`ragtotext.py`)
```bash
docker run -it rag-app python ragtotext.py
```

#### 2. Run the DuckDB RAG Script (`ragtodb.py`)
```bash
docker run -it rag-app python ragtodb.py
```

#### 3. Run the SQLite RAG Script (`ragtosqlite.py`)
```bash
docker run -it rag-app python ragtosqlite.py
```
