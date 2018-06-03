# 描述符 descriptor

Python中的描述符是个什么玩意？

> 一般来说，描述符是一个具有绑定行为的对象属性，其属性的访问被描述符协议方法覆写。这些方法是__get__()、 __set__()和__delete__()，一个对象中只要包含了这三个方法（译者注：包含至少一个），就称它为描述符。

`一句话概括：描述符就是可重用的属性`

## __call__

```python
class Demo(object):

    def __call__(self):
        print('Demo callable')

demo = Demo()
demo()
```

## __iter__


## __len__

```python
class People(object):

    def __init__(self, values=None):
        self._list = values or []

    def __len__(self):
        return len(self._list)

people = People(values=['tommao', 'silence'])

print( len(people) )
```

## __set__ and __get__

```python

```

