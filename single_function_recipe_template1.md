# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

"As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute."

Note:
Function that counts number of words and returns the number of minutes required to read the text. (200w/min rounded up)

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def read_time_calculator(mixed_words):
    """Counts words in a text and returns minutes required to read the text at a rate of 200/min

    Parameters: a string containing words (e.g. "hello WORLD")

    Returns: a number, integer (e.g. ["34"])

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
It returns a number
"""
read_time_calculator("I need fruits") => 1

"""
Given a long text
It returns a number
"""
read_time_calculator("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce a iaculis lorem. Duis fermentum est sit amet sem bibendum condimentum. Nulla ullamcorper nisl nisl, eu porta mauris feugiat eu. Sed nec luctus nisi, ut ornare odio. Ut varius lacus non felis molestie ultricies. Nunc turpis est, maximus in elit at, rutrum vulputate nisi. Maecenas tempor nulla non nisi aliquet, vel feugiat ligula consectetur. Aenean ac turpis non lorem condimentum posuere. Aenean quis ex quis justo tincidunt eleifend. Nullam sit amet leo tempor, tincidunt lorem nec, accumsan neque. Donec mauris augue, consequat sit amet gravida a, pellentesque id erat. Cras vitae est justo. Pellentesque ut augue ac felis ullamcorper placerat. Vivamus euismod purus eget lorem porttitor dignissim. Curabitur turpis est, luctus condimentum cursus non, finibus vel eros. Nam quis felis enim. Nullam aliquet sollicitudin sodales. Nam dolor velit, vehicula eget mollis nec, aliquam at sapien. Cras nec mattis ipsum. Curabitur sed feugiat felis. Mauris facilisis tincidunt nisl in pretium. Donec varius felis at posuere consectetur. Suspendisse potenti. Pellentesque consequat ex faucibus tortor finibus finibus nec a ligula. Pellentesque consectetur auctor augue sed accumsan. Nulla viverra mattis venenatis. Nam scelerisque, nunc non elementum venenatis, ex urna egestas justo, eu mollis dui enim ac mauris. Curabitur et ullamcorper elit, sit amet volutpat orci. Pellentesque placerat tortor pellentesque, euismod libero in, accumsan metus. In sed nisi quis magna tristique consequat. Morbi placerat pharetra cursus. Proin bibendum est quis pulvinar euismod. Aenean eget diam quis diam dignissim vehicula. In nec convallis sapien. Aenean ultrices finibus dignissim. Aenean hendrerit, nisl vel lacinia suscipit, mauris lorem ultrices ipsum, ac dapibus neque orci sed tellus. Cras metus urna, venenatis at eleifend a, sagittis ac magna. Aliquam vel dolor leo. Suspendisse potenti. Phasellus dignissim gravida justo et convallis.") => 2


"""
Given an empty string
It throws an error
"""
read_time_calculator("") throws an error

"""
Given a None value
It throws an error
"""
read_time_calculator(None) throws an error
```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


```python

from lib.single_function_program1 import *

"""
Given a sentence 
It returns a number
"""
def test_read_time_calculator_returns_one_for_short_text():
    result = read_time_calculator("I need fruits")
    assert result == 1

```

Ensure all test function names are unique, otherwise pytest will ignore them!
