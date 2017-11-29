import logging
from time import time

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger = logging.getLogger()


def log(msg):
    logger.info(msg)


def log_pfx(obj, msg, *args):
    logger.info(obj.__class__.__name__ + '| ' + msg, *args)


class IterationLogger(object):
    def __init__(self, message='Started iteration no.: %s\n Time from previous iteration: %ss\n Time from start: %ss',
                 log_by=1000):
        self.log_by = log_by
        self.num_iter = 0
        self.msg = message
        self.time_started = None
        self.time_this_iter = None

    def next_iter(self):
        if self.time_this_iter is None:
            self.time_this_iter = time()
        if self.time_started is None:
            self.time_started = time()
        self.num_iter += 1
        if self.num_iter % self.log_by == 0:
            dur_from_previous = time() - self.time_this_iter
            self.time_this_iter = time()
            dur_from_start = time() - self.time_started
            log_pfx(self, self.msg, str(self.num_iter), str(dur_from_previous), str(dur_from_start))
