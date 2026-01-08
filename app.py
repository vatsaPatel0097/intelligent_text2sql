import streamlit as st
import pandas as pd

from intelligent_text2sql import Text2SQL

st.set_page_config(page_title="Intelligent Text-to-SQL", layout="centered")

st.title("🧠 Intelligent Text-to-SQL")
st.caption("Offline • Zero-cost • Schema-aware")

# DB path (local)
DB_PATH = "sqlite:///data/sales.db"

@st.cache_resource
def load_engine():
    return Text2SQL(DB_PATH)

engine = load_engine()

query = st.text_input(
    "Ask a question about the database",
    placeholder="e.g. Show top customers by total purchase"
)

if st.button("Run Query") and query:
    with st.spinner("Generating SQL and executing..."):
        result = engine.run(query)

    # Case 1: Clarification needed
    if result.get("needs_clarification"):
        st.warning(result["message"])

    # Case 2: SQL error / hallucination detected
    elif result.get("error"):
        st.error("SQL generation failed safely")
        st.code(result["sql"], language="sql")
        st.write(result["error"])
        st.info(result.get("explanation", ""))

    # Case 3: Success
    else:
        st.subheader("Generated SQL")
        st.code(result["sql"], language="sql")

        st.subheader("Result")
        st.dataframe(result["data"])

        col1, col2 = st.columns(2)
        col1.metric("Confidence", f"{int(result['confidence'] * 100)}%")
        col2.write(result["explanation"])
