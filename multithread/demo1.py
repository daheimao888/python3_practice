# coding=utf-8

from time import sleep, ctime
import threading


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)


if __name__ == '__main__':
    print("---开始---：%s" % ctime())

    singthread = threading.Thread(target=sing)
    dancethread = threading.Thread(target=dance)

    singthread.start()
    dancethread.start()

    while True:
        length = len(threading.enumerate())
        if length <= 1:
            break
        sleep(0.5)
    print("---结束---：%s" % ctime())
