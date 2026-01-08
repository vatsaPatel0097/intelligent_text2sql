from intelligent_text2sql.core.engine import Text2SQL

engine = Text2SQL("sqlite:///data/sales.db")

query = "Show top customers by total purchase"
result = engine.run(query)

print("Generated SQL:")
print(result["sql"])
