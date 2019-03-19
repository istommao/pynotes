# 信号


## 进程间传递信号

```python
# signal_child.py
import os
import signal
import sys
import time

pid = os.getpid()
received = False

def signal_usr1(signum, frame):
    global received
    received = True
    print('CHILD %6s: Received USR1' % pid)
    sys.stdout.flush()

print('CHILD %6s: Setting up signal handler' % pid)
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usr1)
print('CHILD %6s: Pausing to wait for signal' % pid)
sys.stdout.flush()
time.sleep(3)

if not received:
    print('CHILD %6s: Never received signal' % pid)
```
```python
# signal_parent.py
import os
import signal
import subprocess
import time
import sys

proc = subprocess.Popen(['python', 'signal_child.py'])
print('parent: pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
print('parent: signaling child')
sys.stdout.flush()
os.kill(proc.pid, signal.SIGUSR1)
```
