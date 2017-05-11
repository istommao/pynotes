# 列表 list
- `一种可变的容器类型`
- 列表以中括号包裹数据，或者使用list
- Python中的列表实际上是一个变长的数组


[Python列表对象实现原理](https://foofish.net/python-list-implements.html)


![](./_image/2017-01-04-17-00-28.jpg)


## 基本操作

- `添加`
    ```python
    lst = ['hello']

    lst.append('world')
    ```

- `修改`
    ```python
    lst = ['hello', 'world']

    lst[0] = '你好'
    ```


- `移除`

    ```python
    lst = ['hello', 'world']

    lst.remove('hello')
    ```

- `扩展`

    ```python
    lst = ['hello world']

    lst.extend(['你好世界'])
    ```
