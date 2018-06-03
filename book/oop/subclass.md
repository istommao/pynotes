# 子类

## 继承

```python
class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_profile(self):
        print(self.name, self.age)

class FeMale(Person):
    """Female."""


class Male(Person):
    """Male inherit Person."""

me = FeMale('Andy', 22)
me.print_profile()

me = Male('codingcat', 25)
me.print_profile()
```
