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

