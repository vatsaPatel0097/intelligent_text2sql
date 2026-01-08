from intelligent_text2sql.utils.db_utils import get_sqlite_schema
from intelligent_text2sql.utils.schema_formatter import schema_to_text
from intelligent_text2sql.utils.embedding_utils import most_relevant

class Text2SQL:
    def __init__(self, db_url: str):
        self.db_path = db_url.replace("sqlite:///", "")
        self.schema = get_sqlite_schema(self.db_path)

        # one chunk per table
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

        return {
            "relevant_schema": relevant_schema
        }
