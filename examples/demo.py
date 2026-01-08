from intelligent_text2sql.core.engine import Text2SQL

engine = Text2SQL("sqlite:///data/sales.db")

output = engine.run("test")
print(output)
