# 进程

## 进程间通信

- 队列
- 共享内存
- 管道
- 信号
- socket

## subprocess

```python
import subprocess

subprocess.call(['ls', '-l'])
```

```python
import subprocess

# 创建shell进程运行命令
subprocess.call(['ls', '-l'], shell=True)
```


## 与其他命令交互

```python
import sys

sys.stderr.write('sys.stderr start\n')
sys.stderr.flush()

while True:
    line = sys.stdin.readline()
    if not line:
        break
    sys.stdout.write(line)
    sys.stdout.flush()

sys.stderr.write('sys.stderr end\n')
sys.stderr.flush()
```
