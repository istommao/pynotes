# 字符串 str

> 字符串是不可变类型，是由字符组成的序列

## 编码

### Python2

`默认编码 ascii`

> str 与 unicode 都是 basestring的子类

```python
data = u'你好世界!'

data.encode('utf-8')
```


### Python3

`默认编码 utf-8`

> 文本统一使用unicode，二进制数据为bytes; str 与 bytes 相互独立

```python
data = '你好世界!'

data.encode()
```


## 基本操作

`切片/分片`

```python
data = '你好世界'

data[0]    # 下标为0
data[:2]   # 下标为0到下标为1
data[::2]  # 每隔两个元素
```
