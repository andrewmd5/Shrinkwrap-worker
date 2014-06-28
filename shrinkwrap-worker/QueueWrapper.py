from queue import Queue as OldQueue

__all__ = ['Queue']

class Queue(OldQueue):
    def task_done(self):
        "Does nothing in Python 3.4"
        pass

    def join(self):
        "Does nothing in Python 3.4"
        pass
