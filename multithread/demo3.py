import threading
import time


def test():
    for i in range(40):
        print("test is run:", i)
        time.sleep(0.5)


if __name__ == '__main__':
    print("main thread is running")
    t = threading.Thread(target=test)
    # 将子线程设置为保护线程
    t.setDaemon(True)
    t.start()
    time.sleep(2)
    print("main thread is ending")
    exit()