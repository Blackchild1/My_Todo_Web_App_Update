import time
import streamlit as st
import functions
import os


st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)


st.write("# Welcome to TopG Todo App! 👋")
st.markdown(
    """
    ### 👈 You can always read details on your todos using the sidebar!    
 
   """
)

st.write(time.strftime("%b %d, %Y %H:%M"))
todos = functions.get_todos()

for todo in todos:
    todo = todo.strip(' \n')
    if not os.path.exists(f"pages/{todo}.txt"):
        with open(f"pages/{todo}.txt", "w") as file:
            pass


def add_todo():
    my_todo = st.session_state["new_todo"] + "\n"
    todos.append(my_todo)
    functions.write_todos(todos)


def add_doc():
    value = st.session_state["new_todo"]
    my_doc = st.session_state["todo_note"]
    functions.write_doc(my_doc, f"pages/{value}.txt")


new_todos = functions.get_todos("new_todos.txt")

tab1, tab2 = st.tabs(["My Todos", "Completed Todos"])

with tab1:
    st.header("Todos")
    st.subheader("You can move todo by checking the box")
    for index, todo in enumerate(todos):
        str1 = f"{index}. {todo}"

        checkbox = st.checkbox(todo, key=str1)
        if checkbox:
            with st.spinner("Loading..."):
                time.sleep(1)
            st.success("Moved")
            new_todos.append(todo)
            todo = todo.strip(" \n")
            todos.pop(index)
            os.remove(f"pages/{todo}.txt")
            functions.write_todos(todos)
            functions.write_todos(new_todos, "new_todos.txt")
            del st.session_state[str1]
            st.experimental_rerun()

    st.text_input(label="", placeholder="Add new todo...",
                  on_change=add_todo,
                  key='new_todo', label_visibility="hidden")

    st.text_area(label="",
                 placeholder=st.subheader("Add an explanation of what your todo entails"),
                 on_change=add_doc,
                 key="todo_note",
                 label_visibility="hidden"
                 )

with tab2:
    st.header("Todos")
    st.subheader("You can delete todo by checking the box")

    for index, todo in enumerate(new_todos):
        index += 1
        str2 = f"{index}. {todo}"
        checkbox = st.checkbox(todo, key=str2)
        if checkbox:
            with st.spinner("Loading..."):
                time.sleep(1)
            st.success("Deleted")
            new_todos.remove(todo)
            functions.write_todos(new_todos, "new_todos.txt")
            del st.session_state[str2]
            st.experimental_rerun()
