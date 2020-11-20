class Stack(list):
    """ This class implements a Stack data structure using a python list"""

    def __init__(self):
        super().__init__()
        self.stack_list = []

    def push(self, item):
        """ Adds item to the stack"""
        self.stack_list.append(item)

    def pop(self):
        """Takes out the item at the top of the stack
        """
        self.stack_list.pop()

    def print(self):
        """Prints the content of the stack"""
        print(self.stack_list)
