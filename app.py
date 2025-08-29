from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.vector_stores.duckdb import DuckDBVectorStore
from llama_index.core import StorageContext
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
import duckdb
import streamlit as st
from data_loader import TxtFileLoader, DuckDBLoader, SQLiteLoader


# models
Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text")
Settings.llm = Ollama(model="gemma2:2b", temperature=0, request_timeout=360.0)

# UI for data source selection
st.sidebar.title("Data Source")
data_source = st.sidebar.selectbox("Select data source", ["Text File", "DuckDB", "SQLite"])

# load documents based on selection
if data_source == "Text File":
    loader = TxtFileLoader(file_path="./facts.txt")
elif data_source == "DuckDB":
    loader = DuckDBLoader(db_path="ducks.duckdb", table_name="ducks")
elif data_source == "SQLite":
    loader = SQLiteLoader(db_path="places.sqlite", table_name="moz_places")

documents = loader.load_documents()
splitter = TokenTextSplitter(separator="\n", chunk_size=64, chunk_overlap=0)

db_path = "./duck.duckdb"

vector_store = DuckDBVectorStore(
    database_path=db_path,
    config_path="./duck.json"
)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(splitter.get_nodes_from_documents(documents), storage_context=storage_context, show_progress=True)

try:

    # Manually create the file if wrapper fails
    conn = duckdb.connect("./duck.duckdb")
    conn.execute("CREATE TABLE IF NOT EXISTS test (id INTEGER)")
    conn.commit()
    conn.close()
except Exception as e:
    print(f"Persistence attempt: {e}")

query_engine = index.as_query_engine()

# Streamlit UI
st.title("Chat")
st.subheader("Pregunteme Cosas")

# Text input for user query
user_query = st.text_input("Su pregunta", key="query_input")

# Button to submit the query
if st.button("Respuesta") or user_query:
    if user_query:
        response = query_engine.query(user_query)
        # Extract only the response text
        response_text = response.response.strip()  # Get the response text and remove any extra whitespace
        
        # Display the response text
        st.write(response_text)
    else:
        st.write("Please enter a query.")

#try:
#    while True:
#        user_query = input(">>> ")
#        response = query_engine.query(user_query)
#        print(response)
#except KeyboardInterrupt:
#    exit()
