import pytest
from lib.single_function_program1 import *

"""
Given a sentence 
It returns a number
"""
def test_read_time_calculator_returns_one_for_short_text():
    calculator = TimeCalculator()
    result = calculator.read_time_calculator("I need fruits")
    assert result == 1

"""
Given a long text
It returns a number
"""
def test_read_time_calculator_returns_one_for_short_text():
    calculator = TimeCalculator()
    result = calculator.read_time_calculator("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce a iaculis lorem. Duis fermentum est sit amet sem bibendum condimentum. Nulla ullamcorper nisl nisl, eu porta mauris feugiat eu. Sed nec luctus nisi, ut ornare odio. Ut varius lacus non felis molestie ultricies. Nunc turpis est, maximus in elit at, rutrum vulputate nisi. Maecenas tempor nulla non nisi aliquet, vel feugiat ligula consectetur. Aenean ac turpis non lorem condimentum posuere. Aenean quis ex quis justo tincidunt eleifend. Nullam sit amet leo tempor, tincidunt lorem nec, accumsan neque. Donec mauris augue, consequat sit amet gravida a, pellentesque id erat. Cras vitae est justo. Pellentesque ut augue ac felis ullamcorper placerat. Vivamus euismod purus eget lorem porttitor dignissim. Curabitur turpis est, luctus condimentum cursus non, finibus vel eros. Nam quis felis enim. Nullam aliquet sollicitudin sodales. Nam dolor velit, vehicula eget mollis nec, aliquam at sapien. Cras nec mattis ipsum. Curabitur sed feugiat felis. Mauris facilisis tincidunt nisl in pretium. Donec varius felis at posuere consectetur. Suspendisse potenti. Pellentesque consequat ex faucibus tortor finibus finibus nec a ligula. Pellentesque consectetur auctor augue sed accumsan. Nulla viverra mattis venenatis. Nam scelerisque, nunc non elementum venenatis, ex urna egestas justo, eu mollis dui enim ac mauris. Curabitur et ullamcorper elit, sit amet volutpat orci. Pellentesque placerat tortor pellentesque, euismod libero in, accumsan metus. In sed nisi quis magna tristique consequat. Morbi placerat pharetra cursus. Proin bibendum est quis pulvinar euismod. Aenean eget diam quis diam dignissim vehicula. In nec convallis sapien. Aenean ultrices finibus dignissim. Aenean hendrerit, nisl vel lacinia suscipit, mauris lorem ultrices ipsum, ac dapibus neque orci sed tellus. Cras metus urna, venenatis at eleifend a, sagittis ac magna. Aliquam vel dolor leo. Suspendisse potenti. Phasellus dignissim gravida justo et convallis.")
    assert result == 2


"""
Given an empty string
It throws an error
"""
def test_throws_error_when_given_empty_string():
    calculator = TimeCalculator()
    with pytest.raises(Exception) as e: 
        calculator.read_time_calculator('')
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."

"""
Given a None value
It throws an error
"""
def test_throws_error_when_given_none_value():
    calculator = TimeCalculator()
    with pytest.raises(Exception) as e: 
        calculator.read_time_calculator(None)
    error_message = str(e.value)
    assert error_message == "Invalid text, must have at least one character."