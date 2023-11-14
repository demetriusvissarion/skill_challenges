# {{PROBLEM}} Class Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
   => function add_todos() that stores todos to a list
   => function show_todos() that displays all the todos

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
    => function mark_as_complete() that removes todo from the list

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Todos:
    # User-facing properties:
    #   name: string

    def __init__(self, name): 
        # Parameters:
        #   name: string
        # Side effects:
        #   self.list_of_todos = {}
        pass # No code here yet

    def add_todos(self, todo):
        # Parameters:
        #   todo: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the todo to the self.list_of_todos
        pass # No code here yet

    def show_todos(self):
        # Returns:
        #   self.list_of_todos
        pass # No code here yet

    def mark_as_complete(self, todo):
        # Parameters:
        #   todo: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   removes todo from the list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a name and a todo
#show_todos shows the user all the todos
"""
reminder = Todos("Kay")
reminder.add_todos("Walk the dog")
reminder.show_todos() # => "Walk the dog, Kay!"

"""
Given a name and no todo
#show_todos raises an exception
"""
reminder = Todos("Kay")
reminder.show_todos() # raises an error with the message "No todo set."

"""
Given a name and an empty todo
#show_todos still reminds the user to do the todo, even though it looks odd
"""
reminder = Todos("Kay")
reminder.add_todos("")
reminder.show_todos() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
