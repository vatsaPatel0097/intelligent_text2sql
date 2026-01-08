from intelligent_text2sql.utils.db_utils import get_sqlite_schema
from intelligent_text2sql.utils.embedding_utils import most_relevant
from intelligent_text2sql.utils.prompt_builder import build_sql_prompt
from intelligent_text2sql.utils.ollama_client import ask_ollama
from intelligent_text2sql.utils.sql_validator import is_safe_sql
from intelligent_text2sql.utils.sql_executor import execute_sql_safe
from intelligent_text2sql.utils.confidence import compute_confidence
from intelligent_text2sql.utils.sql_explainer import explain_sql
from intelligent_text2sql.utils.sql_cleaner import clean_sql



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
        raw_sql = ask_ollama(prompt)
        sql = clean_sql(raw_sql)


        if not is_safe_sql(sql):
            raise ValueError("Unsafe SQL detected")

        df = execute_sql_safe(self.db_path, sql)

        confidence = compute_confidence(sql)
        explanation = explain_sql(sql)

        return {
            "sql": sql,
            "data": df,
            "confidence": confidence,
    "explanation": explanation
        }
