from lib.single_function_program import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
extract_uppercase("hello WORLD") => ["WORLD"]

"""
Given two uppercase words
It returns a list with both words
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]


def test_given_a_string_of_one_word_returns_the_string():
    result = make_snippet('one')
    assert result == 'one'