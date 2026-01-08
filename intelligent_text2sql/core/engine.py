from intelligent_text2sql.utils.db_utils import get_sqlite_schema

class Text2SQL:
    def __init__(self, db_url: str):
        self.db_path = db_url.replace("sqlite:///", "")
        self.schema = get_sqlite_schema(self.db_path)

    def run(self, query: str):
        return self.schema
