# 集合 set

> set是一组key的集合, 没有重复的元素

### 基本操作

- 添加元素

```python
data = {1, 2, 3}
data.add(4)

>>> {1, 2, 3, 4}
```

- 并集

```python
a = {1, 2}
b = {3}

# 方法一
a | b
# 方法二
a.union(b)

>>> {1, 2, 3}
```

- 交集

```python
a = {1, 2}
b = {1, 3}

# 方法一
a & b

# 方法二

a.intersection(b)

>>> {1}
```

- 差集

```python
a = {1, 3, 5, 7}
b = {2, 4, 5, 9}

# 方法一
a - b

# 方法二
a.difference(b)


>>> {1, 3, 7}
```

- 异或

```python
a = {1, 3}
b = {2, 4}

# 方法一
a ^ b

# 方法二
a.symmetric_difference(b)

>>> {1, 2, 3, 4}
```

- 子集

```python
a = {1, 4}
b = {1, 2, 3, 4}

# 方法一
a <= b

# 方法二
a.issubset(b)

>>> True
```

- 超集

```python
a = {1, 2, 3, 4}
b = {1, 4}

# 方法一
a >= b

# 方法二
a.issuperset(b)

>>> True
```


## 不可变集合 frozenset

```
frozenset({1, 2})
```
