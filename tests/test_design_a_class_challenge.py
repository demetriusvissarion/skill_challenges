import pytest
from lib.design_a_class_challenge import *

"""
Given a name and a track
#show_tracks shows the user all the tracks
"""
def test_given_a_name_shows_all_tracks():
    tracks = Tracks("Demetrius")
    tracks.add_tracks("Rammstein: Du Hast")
    tracks.add_tracks("Rammstein: Mutter")
    result = tracks.show_tracks()
    assert result == "Rammstein: Du Hast, Rammstein: Mutter"


"""
Given a name and no track
#show_tracks raises an exception
"""
def test_given_a_name_throws_error_if_no_tracks():
    tracks = Tracks("Demetrius")
    with pytest.raises(Exception) as e: 
        tracks.show_tracks()
    error_message = str(e.value)
    assert error_message == "No track saved."


"""
Given a name and an empty track
#show_tracks raises an exception
"""
def test_given_a_name_throws_error_if_empty_tracks():
    tracks = Tracks("Demetrius")
    with pytest.raises(Exception) as e: 
        tracks.add_tracks("")
    error_message = str(e.value)
    assert error_message == "No track saved."

