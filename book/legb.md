# 变量作用域与LEGB

> Python的名字空间一个非常核心的内容;
> 其实Python的变量名是一个字符串对象，它所指向的对象才是变量本身;
> 这些(变量名) 名字与所指向的对象构成键值对，名字空间中有很多键值对;
> 而LEGB则是名字空间对查找规则

## LEGB

> LEGB 是4个作用域对简称 分别是:

- Local: 函数内的名字空间
- Enclosing function locals: 外部嵌套函数的名字空间 (如closure)
- Global: 函数所在模块的名字空间(文件)
- Builtin: Python内置模块的名字空间

`Python变量的查找顺序`

```
local -> enclosing -> global -> builtin
```


