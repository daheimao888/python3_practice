import threading

# 创建锁
lock = threading.Lock()


# 定义获取列表值得函数，参数为索引值
def get_value(index):
    # 定义列表
    data_list = [1, 3, 5, 7, 9]
    # 上锁
    lock.acquire()
    # 输出内容
    if index >= len(data_list):
        print("%d 下标越界" % index)
        lock.release()
        return
    print(data_list[index])
    # 解锁
    lock.release()


if __name__ == '__main__':
    # 循环创建子线程访问列表
    for i in range(10):
        t1 = threading.Thread(target=get_value, args=(i, ))
        t1.start()