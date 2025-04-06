import streamlit as st
import functions

todos = functions.get_todos()

#Pobiera dane z inputa
def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader('This is subheader')
st.write("This is st.write shit")
st.write("New")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Dodawaj', placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')


#print("Hello")

#st.session_state