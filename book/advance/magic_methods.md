# 魔术方法

- 类型转换协议
- 容器类协议
- 哈希协议
- 迭代器协议
- 可调用对象协议
- 上下文管理协议


## 描述符 descriptor

Python中的描述符是个什么玩意？

> 一般来说，描述符是一个具有绑定行为的对象属性，其属性的访问被描述符协议方法覆写。这些方法是`__get__()`、 `__set__()`和`__delete__()`，一个对象中只要包含了这三个方法（译者注：包含至少一个），就称它为描述符。

`一句话概括：描述符就是可重用的属性`


### `__set__` and `__get__`

```python
class Animal(object):

    def __init__(self, val=None):
        self.val = val

    def __get__(self, obj, objtype):
        return objtype

    def __set__(self, obj, val):
        self.val = val

an = Animal()
an.name = 'cat'
print(an.name)
```



### `__call__`

```python
class Demo(object):

    def __call__(self):
        print('Demo callable')

demo = Demo()
demo()
```


### `__len__`

```python
class People(object):

    def __init__(self, values=None):
        self._list = values or []

    def __len__(self):
        return len(self._list)

people = People(values=['tommao', 'silence'])

print( len(people) )
```


### `__getitem__` and `__setitem__`

```python
class Zoo(object):

    def __init__(self):
        self._data = {}

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

zoo = Zoo()
zoo['lion'] = 'king'
print(zoo['lion'])
```
