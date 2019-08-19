# Pylint 一些常见问题和解决方案

## pylint
1. pylint 是 python 的代码检查工具，依据标准是 pep8

## 代码错误的一些问题

## pylint 命令配置

--rcfile
指定配置文件

--error-only
仅展示错误信息

--py3k
python3 的移植信息

--ignore
忽略文件/文件夹

--ignore-patterns=


## pylint 的简单介绍
默认的 pylint 配置，和一些参数

## 一些比较常见的错误和解决办法

## 在 python2 升级 python3 中的一些错误
using-cmp-argument
python 2 和 3 的 sort/sorted 方法参数不一样

old-division
python 3 整数除法会返回浮点数了

## 自定义的 pylint 配置和代码风格

## 一些冷门的问题

old-ne-operator (E1607): *Use of the <> operator*
boolean-datetime (W1502): *Using datetime.time in a boolean context.*
