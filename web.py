import streamlit as st
import US2P1functions as fun

todos = fun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    fun.write_todos(todos)



st.title("My Todo App")
st.subheader("This is my To-Do App")
st.write("This app was made to increase your productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=" ", placeholder="Add a new To-do...",
              on_change=add_todo, key="new_todo")