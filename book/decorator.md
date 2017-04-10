# 装饰器


## 什么是装饰器

> Python中的装饰器本质上就是在不改变函数本身的情况下 包装一个函数成为另一个函数的语法糖

## 装饰器有什么用

> 复用代码，DRY

- 日志记录
- 权限验证
- 缓存功能
- ...

## 函数装饰器

```python
def wrapper(func):

    def inner(*args, **kwargs):
        print(func.__name__, *args, **kwargs)
        return func(*args, **kwargs)
    return inner

@wrapper
def print_func(words):
    return words

print_func('Hello decorator!')
```

## 类装饰器

```python
class wrapper:

       def __init__(self, func):
        self._func = func

        def __call__(self):
            print(self._func)
            return self._func()

@wrapper
def func():
    return 'hello'
```


