# 线程

## _thread low level module
```python
import _thread
import time

def calc_time(name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(name, time.ctime(time.time()))

def func():
    _thread.start_new_thread(calc_time, ('thread-1', 3))
    _thread.start_new_thread(calc_time, ('thread-2', 4))

func()
while 1:
    pass

```

## threading high level module

```python
import time
import threading

def main_loop():
    print('Thread %s is running' % (threading.current_thread().name))
    n = 0
    while n < 5:
        n = n + 1
        print('Thread %s  %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s end' % threading.current_thread().name)

print('thread %s is running' % threading.current_thread().name)
t = threading.Thread(target=main_loop, name='LoopThread')
t.start()
t.join()

print('Thread %s is end' % threading.current_thread().name)
```

```python
import logging
import threading

class MyThread(threading.Thread):

    def __init__(self, number, logger):
        threading.Thread.__init__(self)
        self.number = number
        self.logger = logger

    def run(self):
        logger.info('Thread run')

        self.logger.info('execute')


def get_logger():
    logger = logging.getLogger('threading')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler('threading.log')
    fmt = '%(asctime)s - %(threadName)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger


if __name__ == '__main__':
    logger = get_logger()
    for i in range(5):
        thread = MyThread(i, logger)
        thread.setName('线程%s' % i)
        thread.start()
```

## threading.Lock()
```python

```

## GIL

>  GIL全局解释器锁，在多核的环境下 python的多线程只能用到一个核
> 这个是CPython解释器设计的历史遗留问题

## ThreadLocal

```python

```


