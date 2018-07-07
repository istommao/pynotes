# CPython源码学习

## 源码组织结构

```shell
├── Doc               # 文档
├── Grammar       # EBNF描述的语法规则
├── Include      # Python 提供的所有头文件
├── Lib             #  Python 自带的所有标准库 由python语言编写
├── Mac          # For Mac
├── Misc         # 一些不适合放在其他地方的文件就放在这里
├── Modules      # 使用C语言编写的模块
├── Objects        # Python的内建对象
├── Parser          # Python 解释器中的 Scanner和Parser, 对Python代码进行词法分析和语法分析
├── Programs   # 二进制可执行文件的源文件
├── Python          # Python 解释器中的Compiler和执行引擎部分，Python运行的核心
└── Tools         # 一些工具
```

## 学习目录

- 解释器源码
- python代码执行过程
- Frame function code object bytecode 等
- Python对象协议
- Python数据类型
- 垃圾回收
- 内存管理
