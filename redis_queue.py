# redis_queue.py


import uuid
import pickle


class Queue(object):
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name

    def enqueue(self, func, *args):
        task = Task(func, *args)
        pickled_task = pickle.dumps(task, protocol=pickle.HIGHEST_PROTOCOL)
        self.conn.lpush(self.name, pickled_task)
        return task.id

    def dequeue(self):
        _, compact_task = self.conn.brpop(self.name)
        task = pickle.loads(compact_task)
        task.process_task()
        return task

    def get_length(self):
        return self.conn.llen(self.name)


class Task(object):
    def __init__(self, func, *args):
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args

    def process_task(self):
        self.func(*self.args)
