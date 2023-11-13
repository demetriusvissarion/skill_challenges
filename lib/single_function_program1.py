import math
class TimeCalculator:
    def __init__(self):
        self.words = 1

    def read_time_calculator(self, text):
        if text == None or len(text) <= 0:
            raise Exception("Invalid text, must have at least one character.")
        if len(text) > 0:
            for i in range(0, len(text)):
                if text[i] == " ":
                    self.words += 1
            minutes = math.ceil(self.words / 200)
            return minutes

    
# calculator = TimeCalculator()
# print(calculator.read_time_calculator(""))
# print(calculator.read_time_calculator("I need fruits"))