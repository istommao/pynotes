# 类与对象

> Python中类的 定义 以 关键字 class 开始

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

## 实例化

```python
me = Person('codingcat', 25)
print(me.name, me.age)
```

## 方法

- classmethod
- staticmethod
- instance method

```python
class Person(object):

    maxage = 120

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_profile(self):
        print('instance method: ', self.name, self.age)

    @classmethod
    def print_maxage(cls):
        print('classmethod: ', 'maxage {}'.format(cls.maxage))

    @staticmethod
    def print_input(message):
        print('staticmethod: ', message)
```

```python
Person.print_maxage()
Person.print_input('Hello world')

me = Person('codingcat', 25)
me.print_profile()
```
`output`
```python
classmethod:  Person maxage 120
staticmethod:  Hello world
instance method:  codingcat 25
```
