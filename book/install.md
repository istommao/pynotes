# Python安装

## CentOS编译安装

```shell
yum install wget gcc make
yum install zlib-devel

# 解决 readline 缺失提醒及方向键行为非预期的问题
yum install readline-devel

# 解决 import bz2 报错
yum install  bzip2-devel

# 解决openssl 错误
yum install openssl openssl-devel

# 解决 import sqlite3 报错
yum install sqlite-devel

# 自行选择需要的python版本
wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz

# 解压
xz -d Python-3.6.1.tar.xz
cd Python-3.6.1

./configure
make
make install
```
