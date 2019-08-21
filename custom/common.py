
# pylint: disable=fixme

import logging
class Father:
  def do_sth(self, *args, **kwargs):
    pass

class Son(Father):
  def do_sth(self, arg_1, arg_2, arg_3=0):
    pass

argu = 'name'
str_a = '%s hello world %s hello world %s' %(argu, argu, argu)


class Wizard:
    def __init__(self, argv):
        self.parse_arguments(argv)

    def parse_arguments(self, argv):
        self.name = argv[0]
        self.magic_ability = argv[1]

range_a = range(100)

set_a = set([num for num in range(100) if num % 2])
set_a = {num for num in range(100) if num % 2}

dict_a = dict([(num, num) for num in range(100) if num % 2])
dict_a = {num: num for num in range(100) if num % 2}


try:
    open('file.txt', 'r')
except Exception:
    raise


class Example:
    def calc_time(self):
        return 1 + 2




def func():
    num_a = 1

    # TODO: xxxxx
    # TODO: yyyyy
    num_b = 2

# TODO: zzzzz
