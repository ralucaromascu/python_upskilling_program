import glob
import os
from threading import Thread
from queue import Queue


def count_words_file(file_name, q=None):
    with open(file_name, 'r') as f:
        read_data = f.read()
    if q:
        q.put(len(read_data.split()))
        q.task_done()
    return len(read_data.split())


def count_words_sequential(pathname_pattern):
    total = 0
    files_list = glob.glob(pathname_pattern)
    files_list = [file for file in files_list if os.path.isfile(file)]
    for file in files_list:
        total = total + count_words_file(file)
    return total


def count_words_threading(pathname_pattern):
    my_queue = Queue()
    files_list = glob.glob(pathname_pattern)
    files_list = [file for file in files_list if os.path.isfile(file)]
    for one_file in files_list:
        new_thread = Thread(target=count_words_file, args=(one_file, my_queue))
        new_thread.start()
        new_thread.join()
    my_queue.join()
    return sum([my_queue.get() for _ in range(len(files_list))])


if __name__ == '__main__':
    print(count_words_sequential('*.txt'))
    print(count_words_threading('*.txt'))
