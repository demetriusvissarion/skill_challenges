class CheckForTodos:
    def __init__(self):
        self.searched_string = '#TODO'

    def check_for_todos(self, text):
        if text == None or len(text) <= 0:
            raise Exception("Invalid text, must have at least one character.")
        if '#TODO' in text:
            print(text)
            return True
        else:
            return False


    
# check = CheckForTodos()
# print(check.check_for_todos(""))
# print(check.check_for_todos("#TODO: Lorem ipsum dolor sit amet, consectetur adipiscing elit."))