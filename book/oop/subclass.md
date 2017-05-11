# 子类

## 继承

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_profile(self):
        print(self.name, self.age)


class Male(Person):
    """Male inherit Person."""


me = Male('codingcat', 25)
me.print_profile()
```
