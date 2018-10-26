import multiprocessing

import time


def copy_work():
    print("拷贝中....", multiprocessing.current_process().pid)
    time.sleep(0.3)


if __name__ == '__main__':
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(copy_work())
    pool.close()
    pool.join()