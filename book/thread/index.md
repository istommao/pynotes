# 线程

## simple demo

```python
import threading

def worker(num):
    print('Worker: %s' % num)

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()
```

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
        print('Thread %s %s' % (threading.current_thread().name, n))
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

## 线程锁 threading.Lock()

```python
import logging
import random
import threading
import time

class Counter:

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value = self.value + 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

counter = Counter()
for i in range(2):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()

logging.debug('Waiting for worker threads')
main_thread = threading.main_thread()
for t in threading.enumerate():
    if t is not main_thread:
        t.join()
logging.debug('Counter: %d', counter.value)
```

## Re-entrant Locks

```python
import threading

lock = threading.RLock()

print('First try :', lock.acquire())
print('Second try:', lock.acquire(0))
```

## Locks as Context Managers

```python
import threading
import logging


def worker_with(lock):
    with lock:
        logging.debug('Lock acquired via with')


def worker_no_with(lock):
    lock.acquire()
    try:
        logging.debug('Lock acquired directly')
    finally:
        lock.release()


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

lock = threading.Lock()
w = threading.Thread(target=worker_with, args=(lock,))
nw = threading.Thread(target=worker_no_with, args=(lock,))

w.start()
nw.start()
```

## GIL

> GIL全局解释器锁，在多核的环境下 python的多线程只能用到一个核
> 这个是CPython解释器设计的历史遗留问题

## ThreadLocal

```python

```


