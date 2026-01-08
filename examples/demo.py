from intelligent_text2sql.utils.ollama_client import ask_ollama

response = ask_ollama("Write a SQL query to get top 5 products by sales")
print(response)
