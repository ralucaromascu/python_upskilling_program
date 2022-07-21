import glob
from threading import Thread
from queue import Queue


def count_words_sequential(pathname_pattern):
    total = 0
    files_list = glob.glob(pathname_pattern)
    print(files_list)
    for one_file in files_list:
        with open(one_file, 'r') as f:
            read_data = f.read()
        words = read_data.split()
        total += len(words)
    return total


def one_file_count(file_name, q):
    # while True:
    with open(file_name, 'r') as f:
        read_data = f.read()
    q.put(len(read_data.split()))
    q.task_done()


def count_words_threading(pathname_pattern):
    total = 0
    my_queue = Queue()
    files_list = glob.glob(pathname_pattern)
    print(files_list)
    for one_file in files_list:
        new_thread = Thread(target=one_file_count(one_file, my_queue))
        new_thread.setDaemon(True)
        new_thread.start()
    my_queue.join()
    while not my_queue.empty():
        total += my_queue.get()
    return total


if __name__ == '__main__':
    print(count_words_threading('*.txt'))
