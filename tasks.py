# tasks.py

import os
import json
import time
import uuid
import collections

from nltk.corpus import stopwords


def count_words(filename):
    wordcount = collections.Counter()
    common_words = set(stopwords.words('english'))
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    with open(os.path.join(data_dir, filename), 'r') as f:
        for line in f:
            wordcount.update(line.split())
    for word in set(common_words):
        del wordcount[word]
    random_str = uuid.uuid4().hex
    outfile = f'{filename}_{random_str}.txt'
    with open(os.path.join(output_dir, outfile), 'w') as outfile:
         outfile.write(json.dumps(dict(wordcount.most_common(20))))
    time.sleep(2)  # simulate long-running task
    proc = os.getpid()
    print(f'Processed {filename} with process id: {proc}')
