from intelligent_text2sql.core.engine import Text2SQL

engine = Text2SQL("sqlite:///data/sales.db")

query = "Show customer names with total purchase"

result = engine.run(query)

print(result)
