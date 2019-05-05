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

*带参数*

```python
def wrapper(*args, **kwargs):
    print(args, kwargs)

    def wrap(func):

        def _inner(*args, **kwargs):
            return func(*args, **kwargs)
        return _inner

    return wrap

@wrapper('hello', key='key')
def print_func(words):
    return words

print_func('Hello decorator with parameters!')
```

## 类装饰器

```python
class wrapper:

    def __init__(self, func):
        self._func = func

    def __call__(self, *args, **kwargs):
        return self._func(*args, **kwargs)

@wrapper
def func(*args, **kwargs):
    return 'hello class decorator'
```

*带参数*

```python
class wrapper:

    def __init__(self, *args, **kwargs):
        print(args, kwargs)

    def __call__(self, func):

        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        return inner

@wrapper('hello', key='key')
def func():
    return 'hello class decorator  with parameters'
```


## 小示例

`普通写法`

```python
def get_article_detail(uid):
    article = ORM.get_article(uid)

    if article:
        cache.incr('key')

    return article
```

`装饰器写法`
```python
def increase_page_view(func):

    def wrapper(*args, **kwargs):
        obj = func(*args, **kwargs)
        if obj:
            cache.incr(obj.id)
        return obj

    return wrapper


@increase_page_view
def get_article_detail(uid):
    return ORM.get_article(uid)
```
