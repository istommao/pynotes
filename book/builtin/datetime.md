# datetime


## 日期格式化

```python
import datetime
now = datetime.datetime.now()
now.strftime('%Y-%m-%d %H:%M:%S')
>>> 2016-03-15 19:38:17
```


## 字符串转日期

```python
import datetime
datestr = '2016-03-15 19:38:17'
datetime.datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')
>>> datetime.datetime(2016, 3, 15, 19, 38, 17)
```
