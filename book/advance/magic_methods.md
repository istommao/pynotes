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

### `__getattribute__` vs `__getattr__`

> difference-between-getattr-vs-getattribute

[stackoverflow Difference between __getattr__ vs __getattribute__](https://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute)

`__setattr__`使用，可以做对象赋值检查

```python
class Person(object):

    def __setattr__(self, attr, value):
        if not isinstance(value, int):
            raise ValueError('Invalid value "{}"'.format(value))

        super(Person, self).__setattr__(attr, value)

tom = Person()
tom.age = 26

# 抛出异常
tom.age = '26'
```

`__getattr__` 在对象不存在该属性的时候调用

```python
class Person(object):

    def __getattr__(self, attr):
        print('__getattr__', attr)
        return super(Person, self).__getattr__(attr)

tom = Person()
tom.age
```

`__getattribute__`只在新式类中有，对象的所有特性的访问都会调用这个方法。

```python
class Person(object):

    def __getattr__(self, attr):
        print('__getattr__', attr)
        return super(Person, self).__getattr__(attr)

    def __getattribute__(self, attr):
        print('__getattribute__', attr)
        return super(Person, self).__getattribute__(attr)

tom = Person()
tom.age = 26

tom.age
tom.height
```

----

- [Magic Methods](http://farmdev.com/src/secrets/magicmethod/index.html)
- [A-guide-to-pythons-magic-methods](http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue6/a-guide-to-pythons-magic-methods.html)


## 上下文管理器

`普通操作`
```python
fd = open('file.txt', 'w')
fd.write('Hello world!')

fd.close()
```

`使用with关键字`

```python
with open('file.txt', 'w') as fd:
    fd.write('Hello world!')
```

`自定义上下文对象`

```python
class ContextDemo(object):

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_value, trace_back):
        print('__exit__', exc_type, exc_value, trace_back)
        return True

    def print(self):
        print('ContextDemo')

with ContextDemo() as f:
    f.print()
```
