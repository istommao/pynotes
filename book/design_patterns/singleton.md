# 单例模式

## 装饰器实现

```python
def singleton(func):

    _auth = None

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal _auth
        if not _auth:
            _auth = func(*args, **kwargs)
        return _auth
    return wrapper


@singleton
def get_auth_instance():
    try:
        auth = AuthInstance(**config)
    except KeyError:
        raise

    return auth
```

## 类实现


```python
class SingletonClass:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
```
