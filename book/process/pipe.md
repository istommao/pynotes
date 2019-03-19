# 管道


## pipe 管道

```python
# 进程单向通信 接收
import subprocess

proc = subprocess.Popen(['echo', '"Hello subproccess PIPE"'],
                        stdout=subprocess.PIPE)
value = proc.communicate()[0]

print(value.decode())
```

```python
# 进程单向通信 发送
import subprocess

proc = subprocess.Popen(['cat', '-'], stdin=subprocess.PIPE)
proc.communicate('Hello PIPE\n'.encode())
```

```python
# 进程双向通信
import subprocess

proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE, stdout=subprocess.PIPE)

msg = 'send message'.encode()
value = proc.communicate(msg)[0]

print('pass throught:', value.decode())
```

```python
# 连接管道段
import subprocess

with open('index.md', 'w') as fd:
    fd.write('#subprocess \n## PIPE')

cat = subprocess.Popen(['cat', 'index.md'], stdout=subprocess.PIPE)

grep = subprocess.Popen(['grep', '#'],
                        stdin=cat.stdout, stdout=subprocess.PIPE)

cut = subprocess.Popen(['cut', '-f', '3', '-d:'],
                       stdin=grep.stdout, stdout=subprocess.PIPE)

for line in cut.stdout:
    print(line.strip().decode())
```


## 创建多个进程

```python
from multiprocessing import Pipe, Process

def spawn_process(data, pipe):
    out_pipe, in_pipe = pipe

    in_pipe.close()
    while True:
        try:
            result = out_pipe.recv()
            print(result)
        except EOFError:
            break


out_pipe, in_pipe = Pipe(True)
sub = Process(target=spawn_process,
              args=('Hello', (out_pipe, in_pipe)))

sub.start()

out_pipe.close()
for i in range(1000):
    in_pipe.send(i)

in_pipe.close()
sub.join()
print('Master process finish!')
```
