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
