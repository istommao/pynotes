# collections

**namedtuple**

>  创建可以用名字访问元素的对象，且新生成的对象具备tuple的不变性

```python
from collections import namedtuple

animal_choices = (
    ('cat', '猫'),
    ('dog', '狗'),
    ('bird', '鸟')
)

tuple_object = namedtuple('Animals', ('cat', 'dog', 'bird'))

Animals = tuple_object(**dict(animal_choices))

print(Animals.cat)
```
