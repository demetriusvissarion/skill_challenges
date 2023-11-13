import pytest
from lib.challenge import *

"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_fails_when_given_a_sentence_without_searched_string():
    check = CheckForTodos()
    result = check.check_for_todos("Curabitur sed feugiat felis")
    assert result == False


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_success_when_given_a_correct_sentence_with_searched_string():
    check = CheckForTodos()
    result = check.check_for_todos("#TODO: Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    assert result == True


"""
Given an empty string
It throws an error
"""
def test_throws_error_when_given_empty_string():
    check = CheckForTodos()
    with pytest.raises(Exception) as e: 
        check.check_for_todos('')
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."

"""
Given a None value
It throws an error
"""
def test_throws_error_when_given_none_value():
    check = CheckForTodos()
    with pytest.raises(Exception) as e: 
        check.check_for_todos(None)
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."