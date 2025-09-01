import sqlite3
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, ToolMessage

con = sqlite3.connect(database="places.sqlite")
cursor = con.cursor()


cursor.execute("PRAGMA table_info(moz_places)")
schema = cursor.fetchall()
schema_str = "column_name type null key default\n" + "\n".join([
    f"{col[1]:<12} {col[2]:<9} {'NO' if col[3] else 'YES'} {'PRI' if col[5] else '':3} {col[4] or 'NULL'}"
    for col in schema
])

@tool
def query(query: str) -> str:
    """Queries the database for information and returns the result.

    Args:
        query: The query to run against the database.
    """
    return str(con.execute(query).fetchone()[0])

llm = ChatOllama(model="qwen2.5-coder").bind_tools([query])

try:
    while True:
        user_query = input(">>> ")
        messages = [
            HumanMessage(
                f"You are provided You are given a SQLite schema for table 'moz_places':\n\n{schema_str}\n\n.\n\nAnswer the user query: '{user_query}' in a single sentence."
            )
        ]
        ai_msg = llm.invoke(messages)
        messages.append(ai_msg)

        for tool_call in ai_msg.tool_calls:
            print(">>> tool_call:", tool_call)
            selected_tool = {"query": query}[tool_call["name"].lower()]
            tool_output = selected_tool.invoke(tool_call["args"])
            print(">>> tool_output:", tool_output)
            messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))

        response = llm.invoke(messages)
        print(response.content)

except KeyboardInterrupt:
    exit()
