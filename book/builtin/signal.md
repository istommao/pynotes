# signal 信号

> 信号是进程之间通讯的一种方式，是一种软件中断

## 常用信号

- SIGINT    终止进程     中断进程  (Control + c)
- SIGTERM   终止进程     软件终止信号
- SIGKILL   终止进程     杀死进程
- SIGALRM   闹钟信号

`示例`

```python
import time

import signal

def handler_signal(signum, frame):
    print('Get signal', signum, frame)

# 注册信号处理函数
signal.signal(signal.SIGINT, handler_signal)

print('wait for Control + c')
time.sleep(5)
```


- SIGHUP
- SIGINT
- SIGQUIT
- SIGILL
- SIGTRAP
- SIGABRT
- SIGEMT
- SIGFPE
- SIGKILL
- SIGBUS
- SIGSEGV
- SIGSYS
- SIGPIPE
- SIGALRM
- SIGTERM
- SIGURG
- SIGSTOP
- SIGTSTP
- SIGCONT
- SIGCHLD
- SIGTTIN
- SIGTTOU
- SIGIO
- SIGXCPU
- SIGXFSZ
- SIGVTALRM
- SIGPROF
- SIGWINCH
- SIGINFO
- SIGUSR1
- SIGUSR2

