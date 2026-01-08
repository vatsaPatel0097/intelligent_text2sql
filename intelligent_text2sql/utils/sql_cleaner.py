import re

def clean_sql(sql: str) -> str:
    if not sql:
        return sql

    # Remove markdown code fences
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)

    # Remove wrapping backticks
    sql = sql.strip()
    if sql.startswith("`") and sql.endswith("`"):
        sql = sql[1:-1]

    # Final strip
    return sql.strip()
