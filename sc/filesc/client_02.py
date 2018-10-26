import socket

# 判断模块是否是程序的入口
if __name__ == '__main__':
    # 1. 创建tcp的客户端socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. 和服务端建立的连接
    tcp_client_socket.connect(("127.0.0.1", 9090))
    # 3. 发送下载文件的请求数据，也就是发送下载的文件名
    file_name = input("请输入您要下载的文件名:")
    tcp_client_socket.send(file_name.encode("utf-8"))

    # 创建文件，以二进制方式向文件写入数据
    try:
        with open("/home/meek/" + file_name, "wb") as file:

            # 通过循环多次接收服务端发送的文件二进制数据
            while True:
                # 循环接收服务端发送的文件二进制数据
                file_data = tcp_client_socket.recv(1024)
                if file_data:
                    # 如果能拿到数据，说明是文件的二进制数据
                    file.write(file_data)
                else:
                    # 如果拿到数据长度为0，说明文件数据发送完成
                    break
    except Exception as e:
        print("下载文件出现异常:", e)
    else:
        print(file_name + " 下载成功")

    # 4. 关闭socket
    tcp_client_socket.close()