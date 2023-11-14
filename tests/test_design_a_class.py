import pytest
from lib.design_a_class import *


"""
Given a name and adding some todos
#show_todos shows the user all his existing todos
"""
def test_given_a_name_shows_all_todos():
    todos = Todos("Demetrius")
    todos.add_todos("Buy fruits")
    todos.add_todos("Take out the rubish")
    result = todos.show_todos()
    assert result == "Buy fruits, Take out the rubish"


"""
Given a name and no todo
#show_todos raises an exception
"""
def test_given_a_name_throws_error_if_no_todos():
    todos = Todos("Demetrius")
    with pytest.raises(Exception) as e: 
        todos.show_todos()
    error_message = str(e.value)
    assert error_message == "No todo set."


"""
Given a name and a todo
#mark_as_complete removes the todo from the list
"""
def test_given_a_name_and_todo_removes_todo():
    todos = Todos("Demetrius")
    todos.add_todos("Buy fruits")
    todos.add_todos("Take out the rubish")
    todos.mark_as_complete("Buy fruits")
    result = todos.show_todos()
    assert result == 'Take out the rubish'


"""
Given a name and an empty todo
#add_todos raises an exception
"""
def test_given_a_name_throws_error_if_no_todos():
    todos = Todos("Demetrius")
    with pytest.raises(Exception) as e: 
        todos.add_todos('')
    error_message = str(e.value)
    assert error_message == "No todo set."

