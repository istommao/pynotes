# 面向对象

## Python对象

> Python中一切皆对象

`Python中所有对象都有2个特性`

- 引用计数
- 类型

```c
typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;
```
