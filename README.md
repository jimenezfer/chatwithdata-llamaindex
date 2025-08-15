Core Purpose:

A persistent RAG (Retrieval-Augmented Generation) system that answers questions about your documents using local AI models with guaranteed database persistence.


RAG System Workflow:

Import libraries - Loads LlamaIndex, DuckDB, and Ollama components for RAG functionality

Configure AI models - Sets up nomic-embed-text for embeddings and gemma2:2b for text generation

Load documents - Reads content from facts.txt file with progress tracking

Split text - Breaks documents into 64-token chunks with no overlap for processing

Set database path - Defines duck.duckdb as the persistent storage filename

Create vector store - Initializes DuckDB vector storage with config from duck.json

Build storage context - Sets up LlamaIndex storage framework around the vector store

Generate embeddings - Converts text chunks into vector embeddings and stores in index

Force persistence - Manually creates duck.duckdb file to bypass LlamaIndex wrapper limitations

Create test table - Ensures database file exists with a simple table structure

Initialize query engine - Sets up the RAG system for interactive question-answering

Start interactive loop - Waits for user questions at the >>> prompt

Process queries - Searches embeddings, retrieves relevant context, generates AI responses

Handle exit - Gracefully exits when user presses Ctrl+C


Key Files Created:

duck.duckdb - Persistent database storing vector embeddings (survives between runs)

duck.json - DuckDB configuration file with memory and performance settings

