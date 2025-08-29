Core Purpose:

A persistent RAG (Retrieval-Augmented Generation) system that answers questions about your documents using local AI models with guaranteed database persistence.

Some examples of chat with .txt,duckdb and sqlite as context.

## Running with Docker

### Build the Docker Image
```bash
docker build -t rag-app .
```

### Run the Applications

You can run any of the three Python scripts using the Docker image.

#### 1. Run the Streamlit Web App (`app.py`)
This is the default command for the Docker container. It will start a web server on port 8501.
```bash
docker run -p 8501:8501 rag-app
```
Open your browser and navigate to `http://localhost:8501` to use the application.

#### 2. Run the DuckDB RAG Script (`ragtodb.py`)
This script runs in the command line.
```bash
docker run -it rag-app python ragtodb.py
```

#### 3. Run the SQLite RAG Script (`ragtosqlite.py`)
This script also runs in the command line.
```bash
docker run -it rag-app python ragtosqlite.py
```


