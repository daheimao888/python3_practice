# coding=utf-8
import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name1, age):
        super(MyThread, self).__init__()
        self.name1 = name1
        self.age = age

    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm" + self.name1 + "@" + str(i)
            print(msg)


if __name__ == '__main__':
    t = MyThread("張三", "18")
    t.start()
