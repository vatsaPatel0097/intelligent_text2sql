import re

def clean_sql(sql: str) -> str:
    # Remove markdown code fences like ```sql ``` or ```
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    # Strip whitespace
    return sql.strip()
