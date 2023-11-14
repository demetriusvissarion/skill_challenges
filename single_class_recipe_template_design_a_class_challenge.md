# {{PROBLEM}} Class Design Recipe


## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
   => function add_tracks to add tracks to a tracks_list
   => function show_tracks to see tracks_list

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class Tracks:
    # User-facing properties:
    #   name: string

    def __init__(self, name): 
        # Parameters:
        #   name: string
        # Side effects:
        #   self.tracks_list = {}
        pass # No code here yet

    def add_tracks(self, track):
        # Parameters:
        #   track: string representing a single track
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the track to the self.tracks_list
        pass # No code here yet

    def show_tracks(self):
        # Returns:
        #   self.tracks_list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
Given a name and a track
#show_tracks shows the user all the tracks
"""
tracks = Tracks("Demetrius")
tracks.add_tracks("Rammstein: Du Hast")
tracks.add_tracks("Rammstein: Mutter")
tracks.show_tracks() # => "Rammstein: Du Hast, Rammstein: Mutter"

"""
Given a name and no track
#show_tracks raises an exception
"""
tracks = Tracks("Demetrius")
tracks.show_tracks() # raises an error with the message "No track set."

"""
Given a name and an empty track
#show_tracks raises an exception
"""
tracks = Tracks("Demetrius")
tracks.add_tracks("")
tracks.show_tracks() # raises an error with the message "No track set."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
