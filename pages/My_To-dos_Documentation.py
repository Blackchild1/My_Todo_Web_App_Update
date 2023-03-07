import streamlit as st
import functions


st.set_page_config(
    page_title="Hello",
    page_icon="✍",
    layout="wide"
)

todos = functions.get_todos()

for todo in todos:
    todo = todo.strip(" \n")
    content = functions.get_doc(f"pages/{todo}.txt")
    st.header(todo)
    st.markdown(content)


