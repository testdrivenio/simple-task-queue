# Asynchronous Task Queues in Python

Several implementations of asynchronous task queues in Python using the multiprocessing library and Redis.

> Blog post: [Developing an Asynchronous Task Queue in Python](http://testdriven.io/developing-an-asynchronous-task-queue-in-python)

## Setup

1. Fork/Clone

1. Create and activate a virtual environment

1. Install the dependencies

1. Enter the Python shell and download the NLTK `stopwords` [corpus](https://www.nltk.org/data.html):

    ```sh
    >> import nltk
    >> nltk.download('stopwords')

      [nltk_data] Downloading package stopwords to
      [nltk_data]     /Users/michael.herman/nltk_data...
      [nltk_data]   Unzipping corpora/stopwords.zip.
      True
    ```

## Examples

Multiprocessing Pool:

```sh
$ python simple_pool.py
```

Multiprocessing Queue:

```sh
$ python simple_queue.py
$ python simple_task_queue.py
```

Logging to a single file:

```sh
$ python simple_task_queue_logging.py
```

Logging to separate files:

```sh
$ python simple_task_queue_logging_separate_files.py
```

Redis:

```sh
$ python redis_queue.py
```
