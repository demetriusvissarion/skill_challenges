import pytest
from lib.drive_class_challenge import *

"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_fails_when_given_a_sentence_ending_without_correct_punctuation():
    check = GrammarStats()
    result = check.check("Curabitur sed feugiat felis")
    assert result == False


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_fails_when_given_a_sentence_starting_with_lowercase():
    check = GrammarStats()
    result = check.check("mauris facilisis tincidunt nisl in pretium?")
    assert result == False


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_success_when_given_a_correct_sentence_ending_with_dot():
    check = GrammarStats()
    result = check.check("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    assert result == True


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_success_when_given_a_correct_sentence_ending_with_exclamation_mark():
    check = GrammarStats()
    result = check.check("Donec varius felis at posuere consectetur!")
    assert result == True


"""
When calling percentage_good function, displays the percentage of texts checked so far that passed the check
It returns an integer representing the percentage
"""
def test_return_percentage_of_success():
    check = GrammarStats()
    result = check.check("Curabitur sed feugiat felis")
    result = check.check("Curabitur sed feugiat felis")
    result = check.check("Curabitur sed feugiat felis.")
    result = check.check("Curabitur sed feugiat felis.")
    result = check.percentage_good()
    assert result == 50

"""
Given an empty string
It throws an error
"""
def test_throws_error_when_given_empty_string():
    check = GrammarStats()
    with pytest.raises(Exception) as e: 
        check.check('')
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."

"""
Given a None value
It throws an error
"""
def test_throws_error_when_given_none_value():
    check = GrammarStats()
    with pytest.raises(Exception) as e: 
        check.check(None)
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."