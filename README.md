# Pylint 一些常见问题和解决方案

## pylint
1. pylint 是 python 的代码检查工具，依据标准是 pep8
2. 在缺省情况下，pylint 会启用很多的规则
3. pylint 的类型推断，使得代码检查得更加全面
3. pylint 有很高的配置性，甚至能够编写插件到自己的检查中
4. pylint [options] modules_or_packages

## 简单的安装

    pip intall pylint

## 错误类型
- (C) convention, 违反了编程的标准，例如 invalid-name (C0103)
- (R) refactor, 有一种代码写挫了的感觉，例如 too-many-branches (R0912)
- (W) warning, python 的具体的问题，例如 dangerous-default-value (W0102)
- (E) error, 可能会造成 bug，例如 not-in-loop (E0103)
- (F) fatal, 发生了阻止 pylint 执行的错误，貌似就一个 method-check-failed (F0202)

## pylint 命令执行的结果
使用了 bit 去标志错误的类型

- 0 if everything went fine
- 1 if a fatal message was issued
- 2 if an error message was issued
- 4 if a warning message was issued
- 8 if a refactor message was issued
- 16 if a convention message was issued
- 32 on usage error

## 代码错误的一些问题

### 变量命名问题

invalid-name (C0103)
blacklisted-name (C0102)

几个命名风格
- snake_case
- camelCase
- PascalCase
- UPPER_CASE

1. 类名使用 PascalCase
2. 参数，局部变量，方法名，类方法名，模块名使用 snake_case，这个 snake_case 是有一个 3-30 的长度限制的
3. 常量需要使用 UPPER_CASE

pylint 配置文档中有两个参数

good-names

    i,j,k,ex,Run,_
bad-names

    foo,bar,baz,toto,tutu,tata
写代码的时候遇上起名困难症，随便取一个意义不明的名字是不行的

```Python
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

```

解决办法：
1. 按照命名风格修改，工作量有点大
2. 在配置中 disable 掉 invalid-name
3. 在配置中修改变量命名的风格
3. 鉴于这些 bad names 确实会让代码意义不明，不要用

### missing-docstring (C0111)
module, function, class or method
模块，方法，类，类方法，都需要 docstring

不能为空，因为还有后手：
empty-docstring (C0112)

解决办法：
1. 加 docstring，工作量真的大
2. 在配置中 disable 掉

### 各式各样的格式问题 Format Checker
bad-whitespace (C0326)
missing-final-newline (C0304)
line-too-long (C0301)
mixed-line-endings (C0327)
too-many-lines (C0302)

还有很多这类的问题，这些问题都比较简单易懂，也很好解决。

解决办法：
1. 找个格式化工具，一键格式化代码
2. 熟练工，了解各类格式问题，亲手格式化！

### 函数的 too-many
在写代码/改代码的时候，函数就可能会变得有很多参数，很多局部变量，很长，很多分支，可能造成一些问题
- too-many-arguments (R0913)
- too-many-locals (R0914)
- too-many-branches (R0912)
- too-many-statements (R0915)

这些问题都是 R 级的问题，不能一味地 diable
解决办法：
1. 拆分成较小的方法
2. 仅对这个方法禁用对应的检查

### 类的 too-many
类也有一些 pylint 的限制，比如类方法数量、类成员数量：
- too-many-ancestors (R0901)
- too-many-instance-attributes (R0902)
- too-few-public-methods (R0903)
- too-many-public-methods (R0904)

类需要有 2-20 个类方法，最多继承 7 个父类，最多有 7 个类成员
也有例外的，
1. 有个设置是 ignore-mixin-members，默认为 yes，忽略了以 mixin 为结尾的类（不区分大小写）
2. 也可以在 ignored-classes 中增加类名

解决办法：
1. disable 了 too-few-public-methods
2. 逐个解决或者禁用其他的问题


### 代码写挫了的更多例子
no-else-raise (R1720) 和 no-else-return (R1705)
```Python
if 1 == 2:
  raise TypeError
elif 2 == 3:
  return 4
else:
  print('error')
```

try-except-raise (W0706)
catch 了 Exception 之后直接 raise，那这个 catch 就没有意义了
```Python
try:
  open('file.txt', 'r')
except Exception:
  raise
```

redefined-builtin (W0622)
```Python
plan_id = 'abc'

def get_plan_id():
  plan_id = 'cde'
  return plan_id
```

len-as-condition (C1801)
其实用 len(list) 也挺好的
```Python
a = []
if len(a) > 0:
  print('a is not empty!')
```

consider-using-set-comprehension (R1718) 和 consider-using-dict-comprehension (R1717)
```Python
set_a = set([num for num in range(100) if num % 2])
set_a = {num for num in range(100) if num % 2}

dict_a = dict([(num, num) for num in range(100) if num % 2])
dict_a = {num: num for num in range(100) if num % 2}
```

### 一些 warning

bad-indentation (W0311) 和 mixed-indentation (W0312)
缩进问题，如果 tab 和 whitespace 混用甚至会导致报错
```Python
# space
def get_my_docstring():
  pass


# tab
def mix_tab_and_space():
	space_line = 0
	tab_line = 1
	print(space_line, tab_line)
```

useless-else-on-loop (W0120)
如果循环里面没有 break，那么这个 else 完全可以移除
```Python
for i in xrange(10):
  if i == 5:
    break
else:
  print('loop done!')
```
protected-access (W0212)
写单元测试的时候会用到，逐个禁用好了
```Python
class Example:
  def __init__(self):
    self._arg = 1

exam = Example()
exam._arg = 3
```

dangerous-default-value (W0102)
当用一个 list 或者 dict 作为参数默认值时，会有问题
```Python
def dangerous_default(default_users=[]):
  default_users.append(1)
  print(default_users)
```

unnecessary-pass (W0107)
一些情况会使得 pass 没有意义
```Python
def useless_pass():
  """"""
  pass
```

wildcard-import (W0401)
```Python
from module import *
```
arguments-differ (W0221)
重写父类的方法时参数数量不一致

```Python
class Father:
  def do_sth(self, *args, **kwargs):
    pass

class Son(Father):
  def do_sth(self, arg_1, arg_2):
    pass
```


### python 3 的检查

pylint 也对 python 3 的兼容做了检查，这类的问题特别多，甚至可以直接看文档中的：Python3 checker Messages
例子：

long-suffix (E1606)
```Python
num = 1L  # python 2
num = 1  # python 3
```

print-statement (E1601)
```Python
print(a, b) 
# 在 python 2 中等价于
print (a, b)

print a, b  # 在 python 3 中会报错
```

old-division
python 3 整数除法会返回浮点数了
```Python
div = 5 / 3  # in Python 2, div = 1; in Python 3, div = 1.66667
div = 5 // 3 # in Python 2 and 3, div = 1;
```

dict-items-not-iterating (W1654)
python 2 和 3 的 items 返回的结果是不一样的
```Python
dict_a = {1: 2, 2: 3}

# Python 2
# >>> type(dict_a.items())
# <type 'list'>

# Python 3
# >>> type(dict_a.items())
# <class 'dict_items'>
```

assign-to-new-keyword (W0111)
```Python
async = 1
```

no-self-use (R0201)
```Python
class Example:
  def calc_time(self):
    return 1 + 2

```

inherit-non-class (E0239)
新式类的问题
```Python
class Example(object):
  pass
```

using-cmp-argument (W1640)
python 2 和 3 的 sort/sorted 方法参数不一样
```Python
sorted(iterable, cmp=None, key=None, reverse=False)  # python 2
sorted(iterable, key, reverse)  # python 3
```

deprecated-method (W1505)
调用了将被废弃的方法，比如 inspect 的 getargspec [inspect 文档](https://docs.python.org/3/library/inspect.html#inspect.getargspec)
```Python
import inspect

arg_spec = inspect.getargspec(func)  # 在 python 3.6 中被替代了
arg_spec = inspect.getfullargspec(func)
```

## 一些有趣的问题

old-ne-operator (E1607):
```Python
1 <> 2
```

boolean-datetime (W1502):
*Using datetime.time in a boolean context.*
```Python
from datetime import time
# boolean-datetime before python 3.5
def is_midnight():
    if not time():
        return True
    return False
```

## pylint 配置文件

可以通过命令来生成一份模板配置

    pylint --generate-rcfile


[MASTER]

可以设置一些 pylint 运行时需要的一些参数

[MESSAGES CONTROL]

disable 和 enable 报错的内容

[REPORTS]

pylint 的结果报表参数，代码评分的计算公式

[BASIC]

命名和 docstring 的设置

[DESIGN]

设置方法的参数数量，类的各种参数数量设置

## pylint 的注释

pylint 注释生效的范围是缩进块中 pylint 注释位置到缩进块结束

```Python
# pylint: disable=fixme
def func():
  num_a = 1
  # TODO: xxxxx
  num_b = 2
  # TODO: yyyyy

# TODO: zzzzz
```
如果需要整个文件都生效，可以在文件开头的地方添加 pylint 的注释
