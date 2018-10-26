# coding=utf-8

from time import sleep, ctime
import threading


def sing(a, b, c):
    print("----sing----a = %d, b = %d,c = %d" % (a, b, c))
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)


if __name__ == '__main__':
    print("---开始---：%s" % ctime())

    # singthread = threading.Thread(target=sing, args=(10, 100, 1000))
    # singthread = threading.Thread(target=sing, kwargs={"a": 10, "b": 100, "c": 1000})
    singthread = threading.Thread(target=sing, args=(10,), kwargs={"b": 100, "c": 1000})

    dancethread = threading.Thread(target=dance)

    singthread.start()
    dancethread.start()

    while True:
        length = len(threading.enumerate())
        if length <= 1:
            break
        sleep(0.5)
    print("---结束---：%s" % ctime())
