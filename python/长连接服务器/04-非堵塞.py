import socket
import time 

client_list = list()
def main():
    # 创建套接字
    s_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s_tcp.bind(("",7890))
    s_tcp.listen(128)
    s_tcp.setblocking(False)

    while True:
        time.sleep(0.5)
        try:
            s_client,addr_client = s_tcp.accept()
        except Exception as ret:
            print("---没有新的客户端到来---")
        else:
            print("---新的客户端到来---")
            s_client.setblocking(False)
            client_list.append(s_client)

        for client in client_list:
            try:
                recv_data = client.recv(1024)  # error:这里发了数据还是产生异常
            except Exception as ret:
                # print(ret)
                print("---客户端还没发送数据---")
            else:
                print("---发送过来了数据---")
                # 对方调用close导致recv为空
                if not recv_data:
                    client_list.remove(client)
                    client.close()  # 关闭套接字
                    print("---客户端已关闭---")


if __name__ == "__main__":
    main()
