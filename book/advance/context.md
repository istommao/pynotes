# 上下文管理器

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
