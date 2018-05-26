# 进程

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
sub = Process(target=spawn_process, args=('Hello', (out_pipe, in_pipe)))

sub.start()

out_pipe.close()
for i in range(1000):
    in_pipe.send(i)

in_pipe.close()
sub.join()
print('Master process finish!')

```
