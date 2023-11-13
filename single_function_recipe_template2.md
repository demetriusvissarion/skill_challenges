# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

"As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark."

Note:
One function to verify that a text starts with a capital letter
Second function to verify that a text ends with a suitable sentence-ending punctuation mark ('.', '?', '!')

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def improve_grammar(mixed_words):
    """
    Verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark

    Parameters: a string containing a sentence (e.g. "I need fruits")

    Returns: a boolean, True or False

    Side effects:
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python

"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
improve_grammar("Curabitur sed feugiat felis") => False


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
improve_grammar("mauris facilisis tincidunt nisl in pretium?") => False


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
improve_grammar("Lorem ipsum dolor sit amet, consectetur adipiscing elit.") => True


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
improve_grammar("Donec varius felis at posuere consectetur!") => True


"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
improve_grammar("Cras nec mattis ipsum?") => True


"""
Given an empty string
It throws an error
"""
improve_grammar("") throws an error


"""
Given a None value
It throws an error
"""
improve_grammar(None) throws an error
```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```python

from lib.single_function_program2 import *

"""
Given a sentence 
It returns True if a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark, or else False
"""
def test_fails_when_given_a_sentence_ending_without_correct_punctuation():
    result = improve_grammar("Curabitur sed feugiat felis")
    assert result == False

```

Ensure all test function names are unique, otherwise pytest will ignore them!
