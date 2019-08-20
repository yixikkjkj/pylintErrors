# Pylint 一些常见问题和解决方案

## pylint
1. pylint 是 python 的代码检查工具，依据标准是 pep8
2. 在缺省情况下，pylint 会启用很多的规则
3. pylint 有很高的配置性，甚至能够编写插件到自己的检查中
4. pylint [options] modules_or_packages

### 错误类型
- (C) convention, 违反了编程的标准，例如 invalid-name (C0103)
- (R) refactor, 有一种代码写挫了的感觉，例如 too-many-branches (R0912)
- (W) warning, python 的具体的问题，例如 dangerous-default-value (W0102)
- (E) error, 可能会造成 bug，例如 not-in-loop (E0103)
- (F) fatal, 发生了阻止 pylint 执行的错误，貌似就一个 method-check-failed (F0202)

### pylint 命令执行的结果
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

pylint 配置中有两个列表
good-names

    i,j,k,ex,Run,_
bad-names

    foo,bar,baz,toto,tutu,tata
写代码的时候遇上起名困难症，随便取一个意义不明的名字是不行的

解决办法：
1. 按照命名风格修改，工作量有点大
2. 在配置中 disable 掉
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

bad-indentation (W0311) 和 mixed-indentation (W0312)
缩进问题，如果 tab 和 whitespace 混用甚至会导致报错

解决办法：
1. 统一缩进方式，不允许出现异类

### 函数的 too-many
在写代码/改代码的时候，函数就可能会变得有很多参数，很多局部变量，很长，很多分支
它们分别是：
too-many-arguments (R0913)
too-many-locals (R0914)
too-many-branches (R0912)
too-many-statements (R0915)

这些问题都是 R 级的问题，不能一味地 diable
解决办法：
1. 拆分成较小的方法
2. 仅对这个方法禁用对应的检查

### 类的 too-many
类也有一些 pylint 的限制，比如类方法数量、类成员数量：
too-many-ancestors (R0901)
too-many-instance-attributes (R0902)
too-few-public-methods (R0903)
too-many-public-methods (R0904)

类需要有 2-20 个类方法，最多继承 7 个父类，最多有 7 个类成员
也有例外的，
1. 有个设置是 ignore-mixin-members，默认为 yes，忽略了以 mixin 为结尾的类（不区分大小写）
2. 也可以在 ignored-classes 中增加类名

解决办法：
1. disable 了 too-few-public-methods
2. 逐个解决或者禁用其他的问题

### protected-access (W0212)

写单元测试的时候会用到，逐个禁用好了

### python 3 的检查
pylint 也对 python 3 的兼容做了检查，这类的问题特别多，可以直接看文档：Python3 checker Messages
例子：
using-cmp-argument
python 2 和 3 的 sort/sorted 方法参数不一样

old-division
python 3 整数除法会返回浮点数了

dict-items-not-iterating (W1654)
python 2 和 3 的 items 返回的结果是不一样的

## 自定义的 pylint 配置和代码风格

## 一些有趣的问题

old-ne-operator (E1607): *Use of the <> operator*
boolean-datetime (W1502): *Using datetime.time in a boolean context.*
