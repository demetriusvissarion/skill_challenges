# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

"As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO."

Note:
One function to check if a text includes the string #TODO."

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def check_for_todos(text):
    """
    Verify if a text includes the string #TODO

    Parameters: a string (e.g. "I need fruits")

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
It returns True if a text includes the string #TODO, or else False
"""
check_for_todos("Curabitur sed feugiat felis") => False


"""
Given a sentence 
It returns True if a text includes the string #TODO, or else False
"""
check_for_todos("Lorem ipsum dolor sit amet, conse#TODOctetur adipiscing elit.") => True


"""
Given an empty string
It throws an error
"""
check_for_todos("") throws an error


"""
Given a None value
It throws an error
"""
check_for_todos(None) throws an error
```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```python

from lib.test_challenge import *

"""
Given a sentence 
It returns True if a text includes the string #TODO, or else False
"""
def test_fails_when_given_a_sentence_without_searched_string():
    result = check_for_todos("Curabitur sed feugiat felis")
    assert result == False

```

Ensure all test function names are unique, otherwise pytest will ignore them!
