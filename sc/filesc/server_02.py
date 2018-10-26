import socket

# 判断模块是否是程序的入口
if __name__ == '__main__':
    # 创建tcp服务端socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_server_socket.bind(("127.0.0.1", 9090))
    # 把服务端socket由主动套接字改成被动套接字，只能接收客户端的连接请求
    tcp_server_socket.listen(128)
    while True:
        # 接收客户端的连接请求， 提示： 现在的下载方式是按照用户连接的顺序进行一个下载，
        # 解决问题需要等后面学习线程的时候去解决
        service_client_socket, ip_port = tcp_server_socket.accept()
        print(ip_port)
        # 接收下载文件的名字
        file_name_data = service_client_socket.recv(1024)
        # 解码数据
        file_name = file_name_data.decode("utf-8")
        # 根据文件名打开文件，获取文件的二进制数据
        with open("/home/meek/Desktop/" + file_name, "rb") as file:
            while True:
                # 读取文件数据
                file_data = file.read(1024)
                if file_data:
                    # 发送一点数据给客户端
                    service_client_socket.send(file_data)
                else:
                    # 文件数据读完，跳出循环
                    break

        # 终止客户端的服务
        service_client_socket.close()
    # 提示： 服务端的socket可以不关闭
    # 对外不提供连接请求的服务
    tcp_server_socket.close()