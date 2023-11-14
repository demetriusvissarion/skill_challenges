import pytest
from lib.drive_class import *

"""
Given a diary entry (title & contents)
It returns the number of words
"""
def test_given_a_diary_entry_returns_number_of_words():
    calculator = DiaryEntry("Gym", "I completed a day 3 workout")
    result = calculator.count_words()
    assert result == 6


"""
format
Given a diary entry (title & contents)
It returns the entry in the corect format
"""
def test_given_a_diary_entry_returns_it_in_correct_format():
    calculator = DiaryEntry("Gym", "I completed a day 3 workout")
    result = calculator.format()
    assert result == "Gym: I completed a day 3 workout"


"""
Given a diary entry (title & contents), and the speed of the reader in wpm
It returns an estimate of the reading time in minutes for the contents at the given wpm.
"""
def test_given_wpm_returns_reading_time():
    calculator = DiaryEntry("Gym", "I completed a day 3 workout")
    result = calculator.reading_time(200)
    assert result == 1


"""
reading_chunk
Given a diary entry (title & contents), the speed of the reader in wpm and minutes the user has to read
It returns a chunk of the contents that the user could read in the given number of minutes
"""
def test_given_wpm_and_minutes_returns_chunk_to_read():
    calculator = DiaryEntry("Latin Lesson", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras maximus neque ut enim finibus mattis. Pellentesque finibus, neque nec viverra varius, purus neque lobortis enim, vel posuere urna quam quis lorem. Quisque blandit dui sit amet ligula tempor sagittis. Etiam eu vulputate nunc, ut tempor velit. Morbi facilisis pellentesque ex, vitae feugiat eros pellentesque sit amet. Donec in ante aliquet, tincidunt dui sit amet, accumsan dolor. Cras ultrices nisl nunc, quis suscipit est auctor id. Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci. Morbi ut convallis est. Maecenas sed metus nulla. Maecenas rhoncus arcu non vulputate placerat. Suspendisse posuere tincidunt odio, sodales tincidunt velit porttitor a. Vivamus sit amet lorem ac enim dapibus consectetur. Ut laoreet lobortis vestibulum. Nunc ac porta magna, ac scelerisque elit. Donec viverra, enim eget gravida ornare, sapien enim accumsan sapien, id volutpat tellus sem eget felis. Aliquam erat volutpat. Fusce porta sem eget nibh ullamcorper, eu tristique orci feugiat. Vestibulum eros enim, maximus vel dolor a, eleifend sollicitudin mauris. Etiam vel mollis massa. Fusce condimentum lacinia ante, et vulputate sem fringilla eu. Integer fermentum tristique metus et viverra. Nam volutpat dolor vel facilisis porta. Pellentesque aliquet quis elit sit amet fringilla. Nulla rhoncus leo eu velit tincidunt, mattis venenatis magna hendrerit. Sed non euismod tellus, vel faucibus magna. Sed sit amet lectus luctus metus condimentum suscipit sed sed libero. Donec a sapien felis. Vivamus condimentum quis nulla in ultrices. Vestibulum facilisis nibh dolor, ac convallis massa volutpat at. Donec tincidunt interdum ligula, eu elementum sem egestas quis. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed porta suscipit odio quis dignissim. Pellentesque tincidunt convallis tempor. Maecenas mollis mattis lacus, in ultricies arcu lacinia ac.")
    result = calculator.reading_chunk(200, 1)
    print(result)
    assert result == "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras maximus neque ut enim finibus mattis. Pellentesque finibus, neque nec viverra varius, purus neque lobortis enim, vel posuere urna quam quis lorem. Quisque blandit dui sit amet ligula tempor sagittis. Etiam eu vulputate nunc, ut tempor velit. Morbi facilisis pellentesque ex, vitae feugiat eros pellentesque sit amet. Donec in ante aliquet, tincidunt dui sit amet, accumsan dolor. Cras ultrices nisl nunc, quis suscipit est auctor id. Suspendisse pretium gravida commodo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed cursus commodo lacus, vitae efficitur dolor. Aliquam sit amet volutpat magna. Morbi dapibus lorem at turpis luctus imperdiet. Mauris pharetra diam urna, vitae molestie lectus auctor ut. Proin iaculis lacus id augue elementum, sed ullamcorper nibh pharetra. Suspendisse ac ex orci. Morbi ut convallis est. Maecenas sed metus nulla. Maecenas rhoncus arcu non vulputate placerat. Suspendisse posuere tincidunt odio, sodales tincidunt velit porttitor a. Vivamus sit amet lorem ac enim dapibus consectetur. Ut laoreet lobortis vestibulum. Nunc ac porta magna, ac scelerisque elit. Donec viverra, enim eget gravida ornare, sapien enim accumsan sapien, id volutpat tellus sem eget felis. Aliquam erat volutpat. Fusce porta sem eget nibh"


"""
Given an empty string in the diary entry (title or contents)
It throws an error
"""
def test_throws_error_when_given_empty_string():
    calculator = DiaryEntry("Gym", "")
    with pytest.raises(Exception) as e: 
        calculator.count_words()
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'contents' must have at least one character."


"""
Given a None value
It throws an error
"""
def test_throws_error_when_given_none_value():
    calculator = DiaryEntry("Gym", None)
    with pytest.raises(Exception) as e: 
        calculator.count_words()
    error_message = str(e.value)
    assert error_message == "Invalid entry, 'title' and 'contents' must have at least one character."