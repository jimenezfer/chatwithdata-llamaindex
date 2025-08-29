from abc import ABC, abstractmethod
from llama_index.core import SimpleDirectoryReader
import duckdb
import sqlite3
import pandas as pd
from llama_index.core.schema import Document
from typing import List

class DataSourceLoader(ABC):
    @abstractmethod
    def load_documents(self) -> List[Document]:
        """Load documents from a data source."""
        pass

class TxtFileLoader(DataSourceLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_documents(self) -> List[Document]:
        """Load documents from a text file."""
        reader = SimpleDirectoryReader(input_files=[self.file_path])
        return reader.load_data(show_progress=True)

class DuckDBLoader(DataSourceLoader):
    def __init__(self, db_path: str, table_name: str):
        self.db_path = db_path
        self.table_name = table_name

    def load_documents(self) -> List[Document]:
        """Load documents from a DuckDB database."""
        con = duckdb.connect(database=self.db_path)
        df = con.execute(f"SELECT * FROM {self.table_name}").fetchdf()
        con.close()
        documents = []
        for _, row in df.iterrows():
            documents.append(Document(text=str(row.to_dict())))
        return documents

class SQLiteLoader(DataSourceLoader):
    def __init__(self, db_path: str, table_name: str):
        self.db_path = db_path
        self.table_name = table_name

    def load_documents(self) -> List[Document]:
        """Load documents from a SQLite database."""
        con = sqlite3.connect(database=self.db_path)
        df = pd.read_sql_query(f"SELECT * FROM {self.table_name}", con)
        con.close()
        documents = []
        for _, row in df.iterrows():
            documents.append(Document(text=str(row.to_dict())))
        return documents
