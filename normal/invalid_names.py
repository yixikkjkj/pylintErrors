# invalid-name
import logging

logger = logging.getLogger(__name__)  # constant

def GetMeow():  # function
    numList = [Xxx for Xxx in range(100) if Xxx % 2]  # varible
    print('Meow')


class person(object):  # classname
    def __init__(self, *args):
        self.Args = args  # attribute

    def setUp(self):
        pass

    def Print_Args(self, Argument1):  # method, argument
        print(self.Args)
        self.o = 1

        for o in range(10):
            print(o)


# good/bad-name
def Run():
    foo = 1
    for i in range(10):
        print(i)


# empty-docstring
def get_my_docstring():
    """"""
    pass


# mixed-indentation
def mix_tab_and_space():
	space_line = 0
	tab_line = 1
	print(space_line, tab_line)


# boolean-datetime before python 3.5
def is_midnight():
    if not time():
        return True
    return False
