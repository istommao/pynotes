# 递归优化

```python
data = {}
def fib(n):
    if n in data:
        return data[n]
    if n < 2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    data[n] = result
    return result
```
