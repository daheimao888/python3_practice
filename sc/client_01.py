# 1、导入socket模块
import socket
# 2、创建socket
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 3、建立tcp连接
tcp_client_socket.connect(("127.0.0.1", 7788))
# 4、开始发送数据
tcp_client_socket.send("哈哈哈，打不过我吧！？".encode("utf-8"))

# 开始接收对方回复的数据
recv_data = tcp_client_socket.recv(1024)
print("接收到数据：", recv_data.decode("utf-8"))

# 5、关闭套接字
tcp_client_socket.close()