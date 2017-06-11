# 函数编程

> Python中的函数也是对象，可以作为其他函数的的参数或返回值

**高阶函数**

> 接受函数为参数，或将函数作为返回值的函数是高阶函数

*示例*
- map
- filter
- reduce  Python3后不再是内置函数，需要从 functools 中导入


## 主要内容

- 堆栈帧 stack frame
- 匿名函数 lambda
- 递归
- 闭包
- 装饰器

## 示例

> Python函数以def关键字定义

```python
def func():
    return 'Hello world'
```

![](./_image/2017-01-04-17-09-50.jpg)

## 一个简单的计算
```python
def mul(a, b):
    return a * b

mul(3, 5)
```

![](./_image/2017-01-04-17-12-16.jpg)
