"""test A"""
from datetime import datetime, time

import logging

logger = logging.getLogger(__name__)

def show_maru():
    """1"""
    pass

def ShowMaru():
    pass

hello = 'hello'
world = 'world'

a = tuple([1])

assert bool(a)

def danger_default(danger={}):
    print(danger)

id = 3

# assign-to-new-keyword
async = 3

# eval-used / exec-used
plus_result = eval('1+2')


# unnecessary-pass
def print_args(*args):
    print(args)
    pass


constant_val = 0

if constant_val:
    print(constant_val)


def after_plan_setted():
    user_id = 'abc'
    plan_id = 'abc'
    now = datetime.now()
    message = 'this message is used to show the logger argument length.'
    args = {
        'user_id': user_id,
        'plan_id': plan_id,
        'now': now,
        'message': message,
    }

    logger.exception('User [%(user_id)s] Plan [%(plan_id)s] setted at [%(now)s], message [%(message).20s] ', args)


if __name__ == "__main__":
    after_plan_setted()


try:
    open('__init__.py', 'rc')
except Exception as exce:
    print(exce)

print(exce)

class classname:
    def __init__(self, args):
        self.args = args


def cannot_assign():
    class CannotAssign:
        def __setitem__(self, key, val):
            pass

    cannot = CannotAssign()
    cannot.sign = 1
