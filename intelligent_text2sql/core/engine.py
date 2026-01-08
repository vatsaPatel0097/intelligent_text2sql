from intelligent_text2sql.utils.db_utils import get_sqlite_schema
from intelligent_text2sql.utils.schema_formatter import schema_to_text

class Text2SQL:
    def __init__(self, db_url: str):
        self.db_path = db_url.replace("sqlite:///", "")
        self.schema = get_sqlite_schema(self.db_path)
        self.schema_text = schema_to_text(self.schema)

    def run(self, query: str):
        return {
            "schema": self.schema,
            "schema_text": self.schema_text
        }
