from stack import Stack
import unittest


class StackTest(unittest.TestCase):

    def test_push_to_stack(self):
        stack = Stack()
        item = "Daily Sun"
        stack.push(item)
        self.assertIn(item, stack)


unittest.main()
