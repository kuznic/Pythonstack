from stack import Stack
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
        self.daily_sun = "Daily Sun"
        self.daily_planet = "Daily Planet"

    def test_push(self):
        """This is testing the push function in stack.py module that is implementing a stack data structure as a List"""
        self.stack.push(self.daily_sun)
        self.assertIn(self.daily_sun, self.stack.stack_list)
        self.assertNotIn(self.daily_planet, self.stack.stack_list, " in stack")

    def test_pop(self):
        """This is testing that items are removed from the top of the stack"""
        self.stack.push(self.daily_planet)
        self.stack.pop()
        self.assertNotIn(self.daily_planet, self.stack.stack_list)

    def test_instance(self):
        self.assertIsInstance(self.stack, Stack)

        if __name__ == '__main__':
            unittest
