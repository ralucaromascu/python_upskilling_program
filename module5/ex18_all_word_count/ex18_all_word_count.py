import glob
import os
from threading import Thread
from queue import Queue


def count_words_file(file_name, q):
    with open(file_name, 'r') as f:
        read_data = f.read()
    q.put(len(read_data.split()))
    q.task_done()


def queue_sum(q):
    total = 0
    while not q.empty():
        total += q.get()
    return total


def count_words_sequential(pathname_pattern):
    my_queue = Queue()
    files_list = glob.glob(pathname_pattern)
    files_list = [file for file in files_list if os.path.isfile(file)]
    for file in files_list:
        count_words_file(file, my_queue)
    return queue_sum(my_queue)


def count_words_threading(pathname_pattern):
    my_queue = Queue()
    files_list = glob.glob(pathname_pattern)
    files_list = [file for file in files_list if os.path.isfile(file)]
    for one_file in files_list:
        new_thread = Thread(target=count_words_file, args=(one_file, my_queue))
        new_thread.start()
        new_thread.join()
    my_queue.join()
    return queue_sum(my_queue)


if __name__ == '__main__':
    print(count_words_threading('*.txt'))
