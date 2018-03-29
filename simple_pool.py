# simple_pool.py

import time
import multiprocessing

from tasks import get_word_counts


PROCESSES = multiprocessing.cpu_count() - 1


def run():
    print(f'Running with {PROCESSES} processes!')
    start = time.time()
    with multiprocessing.Pool(PROCESSES) as p:
        p.map_async(get_word_counts, [
            'pride-and-prejudice.txt',
            'heart-of-darkness.txt',
            'frankenstein.txt',
            'dracula.txt'
        ])
        # clean up
        p.close()
        p.join()
    print('Time taken = {0:.10f}'.format(time.time() - start))


if __name__ == '__main__':
    run()
