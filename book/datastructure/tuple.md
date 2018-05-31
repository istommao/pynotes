# 元组 tuple

> 元组以小括号包裹数据

- `(只有一个数据时记得加个逗号，否则它将变成其他类型的数据而不是元组)`
- 元组可以存不同类型的数据
- 元组为不可变对象

![](./_image/2017-01-04-17-01-46.jpg)


```python
data = ('Hello', '世界', 1)

# 元组修改元素会报错
data[0] = '你好'

TypeError: 'tuple' object does not support item assignment
```


```python
data = ('Hello', '世界', 1, [1, 2, 3])

# 修改元组元素中的可变对象不会报错
data[-1] .append(4)
```
