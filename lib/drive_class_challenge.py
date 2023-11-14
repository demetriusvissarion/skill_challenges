import math

class GrammarStats:
    def __init__(self):
        self.true_tracker = 0
        self.false_tracker = 0
        self.sucess_percentage = 0
        

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        end_punctuation = ['.', '!', '?']
        if text == None or len(text) <= 0:
            raise Exception("Invalid text, must have at least one character.")
        elif text[0].istitle() and text[-1] in end_punctuation:
            self.true_tracker += 1
            return True
        else:
            self.false_tracker += 1
            return False
            
        pass

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        self.sucess_percentage = math.ceil(self.true_tracker * 100 / (self.true_tracker + self.false_tracker))
        return self.sucess_percentage