class Text2SQL:
    def __init__(self, db_url: str):
        self.db_url = db_url

    def run(self, query: str):
        raise NotImplementedError("Coming soon")
