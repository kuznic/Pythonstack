from stack import Stack


def stack_test():
    """This is testing the stack.py module that is implementing a stack data
    structure as a List"""
    news_paper_stack = Stack()
    news_paper_stack.push("Daily Sun")
    news_paper_stack.push("Daily Tribune")
    news_paper_stack.print()
    news_paper_stack.pop()
    news_paper_stack.print()
    news_paper_stack.push("Daily Planet")
    news_paper_stack.print()


stack_test()
