from intelligent_text2sql import Text2SQL

engine = Text2SQL(
    "sqlite:///data/sales.db",
    llm_backend="ollama"
)

result = engine.run("Show total sales by customer")

if result.get("needs_clarification"):
    print(result["message"])
elif result.get("error"):
    print(result["error"])
else:
    print(result["sql"])
    print(result["data"])
