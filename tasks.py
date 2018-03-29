# tasks.py

import os
import json
import time
import uuid
import collections

from nltk.corpus import stopwords


COMMON_WORDS = set(stopwords.words('english'))
DATA_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'output')


def save_file(filename, data):
    random_str = uuid.uuid4().hex
    outfile = f'{filename}_{random_str}.txt'
    with open(os.path.join(OUTPUT_DIRECTORY, outfile), 'w') as outfile:
        outfile.write(data)


def get_word_counts(filename):
    wordcount = collections.Counter()
    # get counts
    with open(os.path.join(DATA_DIRECTORY, filename), 'r') as f:
        for line in f:
            wordcount.update(line.split())
    for word in set(COMMON_WORDS):
        del wordcount[word]
    # save file
    save_file(filename, json.dumps(dict(wordcount.most_common(20))))
    # simulate long-running task
    time.sleep(2)
    proc = os.getpid()
    print(f'Processed {filename} with process id: {proc}')


if __name__ == '__main__':
    get_word_counts()
