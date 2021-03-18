# 多进程http服务器
import socket
import re
import multiprocessing
from httpfun.HttpService import *





def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定本地ip
    tcp_server.bind(("",7890))
    # 设置为被动模式(listen)
    tcp_server.listen(5)

    while True:
        # 等待连接(accept),这里会堵塞直到有第一个客户端连接
        print("----waiting for connect----")
        client_socket,client_addr = tcp_server.accept()
        print("----finish connect----")
        p = multiprocessing.Process(target=server_service,
                                    args=(client_socket,client_addr,))
        # 发送数据给客户端
        p.start()
        # 主进程关闭套接字
        client_socket.close()

    tcp_server.close()

if __name__ == "__main__":
    main()
