from stack import Stack


def stack_test():
    """This is testing the stack.py module that is implementing a stack data
    structure as a List"""
    news_paper_stack = Stack()
    news_paper_stack.add_to_stack("Daily Sun")
    news_paper_stack.add_to_stack("Daily Tribune")
    news_paper_stack.print_stack()
    news_paper_stack.remove_from_stack()
    news_paper_stack.print_stack()
    news_paper_stack.add_to_stack("Daily Planet")
    news_paper_stack.print_stack()


stack_test()
