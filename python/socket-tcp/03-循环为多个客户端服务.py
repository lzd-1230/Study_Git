import socket


def main():
    # 1.创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 2.绑定本地ip
    tcp_server.bind(("",7890))

    # 3.设置为被动模式(listen)
    tcp_server.listen(128)  # 128代表最多可以和多少个客户端通信
    
    # 4.等待连接(accept),这里会堵塞直到有第一个客户端连接
    while True:
        print("----waiting for connect----")
        client_socket,client_addr = tcp_server.accept()
        print("----finish connect----")
        print(client_addr)
        while True:
            recv_data = client_socket.recv(1024)
            # 判断客户端是否关闭
            if recv_data:
                print(recv_data.decode("gbk"))
            else:
                break
        #6.关闭人工服务的套接字
        client_socket.send("-----------已经服务完毕----------".encode("gbk"))
        client_socket.close()
        print("已经服务完该客户端")

    tcp_server.close()
if __name__ == "__main__":
    main()
