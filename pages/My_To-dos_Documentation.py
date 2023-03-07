import streamlit as st
import functions


todos = functions.get_todos()

for todo in todos:
    todo = todo.strip(" \n")
    content = functions.get_doc(f"pages/{todo}.txt")
    st.header(todo)
    st.markdown(content)


