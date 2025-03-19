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
tar xf Python-3.6.1.tar.xz

# xz -d Python-3.6.1.tar.xz
cd Python-3.6.1



./configure
make
make install
```

## Ubuntu编译安装

```bash
wget https://www.python.org/ftp/python/3.13.2/Python-3.13.2.tar.xz


sudo apt install -y zlib1g zlib1g-dev libffi-dev openssl libssl-dev
sudo apt-get install bzip2 libbz2-dev sqlite3 libsqlite3-dev libreadline6 libreadline6-dev libgdbm-dev uuid-dev tk-dev

./configure
make
make install
```



## 国内源

Python源码 https://npm.taobao.org/mirrors/python

[Python Mirror](https://npm.taobao.org/mirrors/python)

PyPI源 

https://mirrors.aliyun.com/pypi/simple/

[Simple Index](https://mirrors.aliyun.com/pypi/simple/)

```bash
# ~/.pip/pip.conf

[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install]
trusted-host=mirrors.aliyun.com
```

pyenv 安装配置与国内镜像加速 结合 virtualenv

[pyenv 安装配置与国内镜像加速 结合 virtualenv](https://segmentfault.com/a/1190000006174123)

Pyenv安装

```bash
v=3.7.3;wget https://npm.taobao.org/mirrors/python/$v/Python-$v.tar.xz -P ~/.pyenv/cache/;pyenv install $v
```

poetry使用

> PYTHON PACKAGING AND DEPENDENCY MANAGEMENT MADE EASY
> 

https://python-poetry.org/

[Poetry](https://python-poetry.org/)