from lib.music_library import *
import pytest

"""
Instatiates with an empty list stored in self.library
"""
def test_instantiates_correctly():
    music_library = MusicLibrary()
    assert music_library.library == []


"""
Given that a user inputs a valid track
The track is stored in self.library
"""
def test_add_track_with_valid_input():
    music_library = MusicLibrary()
    assert music_library.add_track("example_artist", "example_title") == "Success"
    assert music_library.library == [{"artist": "example_artist", "title": "example_title"}]

"""
Given that a user inputs a track and artist and title arguments are not strings
Returns an error
"""
def test_add_track_with_invalid_input():
    music_library = MusicLibrary()
    with pytest.raises(ValueError) as e:
        music_library.add_track(3, [])
    error_message = str(e.value)
    assert error_message == "Input track artist and title must be strings"

"""
When the list_library method is called
Returns self.library as a list
"""
def test_list_libary_returns_correctly():
    music_library = MusicLibrary()
    music_library.add_track('artist1', 'track1')
    music_library.add_track('artist2', 'track2')
    music_library.add_track('artist3', 'track3')
    assert music_library.list_library() == [
        {"artist": "artist1",
        "title": "track1"
        },
        {"artist": "artist2",
        "title": "track2"
        },
         {"artist": "artist3",
        "title": "track3"
        }
    ]
