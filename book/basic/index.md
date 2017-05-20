# Python基础

> Python中的变量，正确的说应该叫做名字，名字所对应那个才是变量本身。
> 在Python中，名字与对象的映射组成的空间称为名字空间，而这个名字空间，
> 根据作用域的不同而有所不同。

**名字空间**

- Local 本地名字空间
- Enclosing function locals: 外部嵌套函数的名字空间 (如closure)
- Global: 函数所在模块的名字空间(文件)
- Builtin: Python内置模块的名字空间


## 变量赋值

```python
varInt = 1
varStr = 'codingcat'
varFloat = 3.14
varList = [1, 'codingcat', 3.14]
```

### 多重赋值

```python
x = y = z = 1
```

### '多元'赋值

```python
x, y, z = 1, 'codingcat', 3.14
```

## 变量交换

```python
a, b = 1, 2
a, b = b, a
```
