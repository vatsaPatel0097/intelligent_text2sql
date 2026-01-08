from intelligent_text2sql.core.engine import Text2SQL

engine = Text2SQL("sqlite:///data/sales.db")

query = "Show top customers by total purchase"
result = engine.run(query)

print("User Query:", query)
print("Relevant Schema:")
for r in result["relevant_schema"]:
    print("-", r)
