Core Purpose:

A persistent RAG (Retrieval-Augmented Generation) system that answers questions about your documents using local AI models with guaranteed database persistence.

This application can ingest data from multiple sources:
- A text file (`facts.txt`)
- a DuckDB database (`ducks.duckdb`)
- a SQLite database (`places.sqlite`)

## Running with Docker

### Build the Docker Image
```bash
docker build -t rag-app .
```

### Run the Application
This will start a web server on port 8501.
```bash
docker run -p 8501:8501 rag-app
```
Open your browser and navigate to `http://localhost:8501`. Use the sidebar to select the data source you want to chat with.


