class Stack:
    """ This class implements a Stack data structure using a python list"""

    def __init__(self):
        self.stack_list = []

    def add_to_stack(self, item):
        """ Adds item to the stack"""
        self.stack_list.append(item)

    def remove_from_stack(self):
        """Takes out the item at the top of the stack"""
        self.stack_list.pop()

    def print_stack(self):
        """Prints the content of the stack"""
        print(self.stack_list)
