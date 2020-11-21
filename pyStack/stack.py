class Stack:
    """ This class implements a pyStack data structure using a python list"""

    def __init__(self):
        self._stack_list = []  # private attribute

    def push(self, item):
        """ Adds item to the stack"""
        self._stack_list.append(item)

    def pop(self):
        """Takes out the item at the top of the stack
        """
        self._stack_list.pop()

    def get_stack(self):
        """Returns the stack list"""
        return self._stack_list

    def print(self):
        """Prints the content of the stack"""
        print(self._stack_list)
