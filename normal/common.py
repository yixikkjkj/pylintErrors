# import-message
from datetime import time, datetime
from . import test as test

import logging

# invalid-name
logger = logging.getLogger(__name__)  # constant

def GetMeow():  # function
    numList = [Xxx for Xxx in range(100) if Xxx % 2]  # variable
    print('Meow')


class person(object):  # classname
    LEGS = 2
    def __init__(self, *args):
        self.Args = args  # attribute

    def setUp(self):  # method
        pass

    def Print_Args(self, Argument1):  # argument
        print(self.Args)
        args = {
            'user_id': 'abc',
            'now': 123,
            'message': 'shorter length of this log',
        }
        logger.exception('User [%(user_id)s] setted at [%(now)s], message [%(message).20s] ', args)
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
