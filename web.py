import streamlit as st
import function


def add_todo():
    todo=st.session_state["new_todo"]+"\n"
    print(todo)
    todos.append(todo)
    function.write_todos(todos)
    st.session_state["new_todo"]=""


todos=function.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is very useful")

for i, gel in enumerate(todos):
    checkbox=st.checkbox(gel, key=f"todo_{i}")
    if checkbox:
        todos.pop(i)
        function.write_todos(todos)
        st.rerun()

st.text_input(label="",placeholder="Enter a todo",on_change=add_todo,key='new_todo')

