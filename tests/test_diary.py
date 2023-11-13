from lib.diary import *

"""
Given an empty string returns an empty string
"""
def test_given_an_empty_string_returns_an_empty_string():
    result = make_snippet('')
    assert result == ''

"""
Given a string of 1 word returns the string
"""
def test_given_a_string_of_one_word_returns_the_string():
    result = make_snippet('one')
    assert result == 'one'

"""
Given a string of 5 words returns the string
"""
def test_given_a_string_of_five_words_returns_the_string():
    result = make_snippet('one two three four five')
    assert result == 'one two three four five'

"""
Given a string of 6 words returns the first 5 words and 3 dots
"""
def test_given_a_string_of_six_words_returns_the_first_five_words_and_three_dots():
    result = make_snippet('one two three four five six')
    assert result == 'one two three four five...'