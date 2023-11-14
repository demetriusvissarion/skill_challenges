class Todos:
    # User-facing properties:
    #   name: string

    def __init__(self, name): 
        # Parameters:
        #   name: string
        # Side effects:
        #   self.list_of_todos = {}
        self.name = name
        self.todos_list = {}

    def add_todos(self, todo):
        # Parameters:
        #   todo: string representing a single todo
        # Returns:
        #   success text or throws error
        # Side-effects
        #   Saves the todo to the self.list_of_todos
        if len(todo) > 0:
            # if key/value exists append to value, else create key/value
            self.todos_list.setdefault(self.name, []).append(todo)
            print("Todo was added to your list")
        else:
            raise Exception("No todo set.")

    def show_todos(self):
        # Returns:
        #   self.list_of_todos
        if self.todos_list.get(self.name) != None:
            return ', '.join(self.todos_list[self.name])
        else:
            raise Exception("No todo set.")

    def mark_as_complete(self, todo):
        # Parameters:
        #   todo: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   removes todo from the list
        if self.todos_list.get(self.name) != None:
            self.todos_list[self.name].remove(todo)
        else:
            raise Exception("No todo set.")


# todos = Todos("Demetrius")
# todos.add_todos("Buy fruits")
# todos.add_todos("Take out the rubish")
# print(todos.show_todos())

# todos = Todos("Demetrius")
# print(todos.show_todos())

# todos = Todos("Demetrius")
# todos.add_todos("Buy fruits")
# todos.add_todos("Take out the rubish")
# todos.mark_as_complete("Buy fruits")
# print(todos.show_todos())