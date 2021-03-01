import socket


def main():
    # 1.创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2.绑定本地ip
    tcp_server.bind(("",7890))

    # 3.设置为被动模式(listen)
    tcp_server.listen(128)  # 128代表
    
    # 4.等待连接(accept),这里会堵塞直到有第一个客户端连接
    print("----waiting for connect----")
    client_socket,client_addr = tcp_server.accept()
    print("----finish connect----")
    print(client_addr)

    # 5.回送一部分数据
    recv_data = client_socket.recv(1024)
    print(recv_data.decode("gbk"))
    client_socket.send("-----------ok,收到----------".encode("gbk"))

    #6.关闭套接字
    client_socket.close()
    tcp_server.close()
if __name__ == "__main__":
    main()
