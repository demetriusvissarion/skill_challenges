from lib.count_words import *

"""
Given an empty string returns zero
"""
def test_given_an_empty_string_returns_zero():
    result = count_words('')
    assert result == 0

"""
Given a string of 1 word returns 1
"""
def test_given_a_string_of_one_word_returns_one():
    result = count_words('one')
    assert result == 1

"""
Given a string of 6 words returns 6
"""
def test_given_a_string_of_six_words_returns_six():
    result = count_words('one two three four five six')
    assert result == 6