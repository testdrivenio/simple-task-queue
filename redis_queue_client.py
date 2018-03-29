# redis_queue_client.py

import redis

from redis_queue import Queue
from tasks import count_words


NUMBER_OF_TASKS = 10


if __name__ == '__main__':
    r = redis.Redis()
    queue = Queue(r, 'sample')
    count = 0
    for num in range(NUMBER_OF_TASKS):
        queue.enqueue(count_words, 'pride-and-prejudice.txt')
        queue.enqueue(count_words, 'heart-of-darkness.txt')
        queue.enqueue(count_words, 'frankenstein.txt')
        queue.enqueue(count_words, 'dracula.txt')
        count += 4
    print(f'Enqueued {count} tasks!')
