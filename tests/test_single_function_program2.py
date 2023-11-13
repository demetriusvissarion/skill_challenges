import pytest
from lib.single_function_program2 import *

"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_fails_when_given_a_sentence_ending_without_correct_punctuation():
    check = ImproveGrammar()
    result = check.improve_grammar("Curabitur sed feugiat felis")
    assert result == False

"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_fails_when_given_a_sentence_starting_with_lowercase():
    check = ImproveGrammar()
    result = check.improve_grammar("mauris facilisis tincidunt nisl in pretium?")
    assert result == False


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_success_when_given_a_correct_sentence_ending_with_dot():
    check = ImproveGrammar()
    result = check.improve_grammar("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    assert result == True


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_success_when_given_a_correct_sentence_ending_with_exclamation_mark():
    check = ImproveGrammar()
    result = check.improve_grammar("Donec varius felis at posuere consectetur!")
    assert result == True


"""
Given an empty string
It throws an error
"""
def test_throws_error_when_given_empty_string():
    check = ImproveGrammar()
    with pytest.raises(Exception) as e: 
        check.improve_grammar('')
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."

"""
Given a None value
It throws an error
"""
def test_throws_error_when_given_none_value():
    check = ImproveGrammar()
    with pytest.raises(Exception) as e: 
        check.improve_grammar(None)
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."