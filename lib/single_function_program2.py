import math
class ImproveGrammar:
    def __init__(self):
        self.end_punctuation = ['.', '!', '?']

    def improve_grammar(self, text):
        if text == None or len(text) <= 0:
            raise Exception("Invalid text, must have at least one character.")
        elif text[0].istitle() and text[-1] in self.end_punctuation:
            return True
        else:
            return False

    
check = ImproveGrammar()
# print(check.improve_grammar(""))
print(check.improve_grammar("Lorem ipsum dolor sit amet, consectetur adipiscing elit."))