# MusicLibrary Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicLibrary():

    def __init__(self):
        """
        List of dictionaries =>
        self.library = [
            {"artist": str(),
            "title": str()
            },
            ...
        ]
        """
        self.library = []

    def add_track(self, artist, title):
        # Adds track to self.library
        # Arguments:
        #   artist: a string representing the artist of the track
        #   title: a string representing the title of the track
        # Returns:
        #   string: Success/error message
        # Side-effects:
        #   Updates self.library with added track
        pass

    def list_library(self):
        # Arguments:
        #   None
        # Returns:
        #   self.library as a list
        # Side-effects:
        #   None
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
"""
Instatiates with an empty list stored in self.library
"""
music_library = MusicLibrary()
music_library.library => []

"""
Given that a user inputs a valid track
The track is stored in self.library
"""
music_library.add_track("example_artist", "example_title")
music_library.library => [{"artist": "example_artist", "title": "example_title"}]

"""
Given that a user inputs a track and artist and title arguments are not strings
Returns an error
"""
music_library.add_track(3, [])
error_message => "Input track artist and title must be strings"

"""
When the list_library method is called
Returns self.library as a list
"""
music_library.list_library()
=>[
    {"artist": str(),
    "title": str()
    },
    ...
]

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
