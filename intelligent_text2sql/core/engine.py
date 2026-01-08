from intelligent_text2sql.utils.db_utils import get_sqlite_schema
from intelligent_text2sql.utils.embedding_utils import most_relevant
from intelligent_text2sql.utils.prompt_builder import build_sql_prompt
from intelligent_text2sql.utils.ollama_client import ask_ollama

class Text2SQL:
    def __init__(self, db_url: str):
        self.db_path = db_url.replace("sqlite:///", "")
        self.schema = get_sqlite_schema(self.db_path)

        self.schema_chunks = [
            f"Table {table} has columns: " +
            ", ".join([c["column"] for c in cols])
            for table, cols in self.schema.items()
        ]

    def run(self, query: str):
        relevant_schema = most_relevant(
            self.schema_chunks,
            query,
            top_k=2
        )

        prompt = build_sql_prompt(query, relevant_schema)

        sql = ask_ollama(prompt)

        return {
            "sql": sql,
            "used_schema": relevant_schema
        }
