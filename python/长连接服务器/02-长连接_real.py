import socket
import time 
from httpfun.HttpService import *

client_list = list()
def main():
    # 创建套接字
    s_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s_tcp.bind(("",7890))
    s_tcp.listen(128)
    s_tcp.setblocking(False)

    while True:
        try:
            s_client,addr_client = s_tcp.accept()
        except Exception as ret:
            pass
        else:
            s_client.setblocking(False)
            client_list.append(s_client)

        for client in client_list:
            try:
                recv_data = client.recv(1024)  # error:这里发了数据还是产生异常
            except Exception as ret:
                # print(ret)
                pass
            else:
                if recv_data:
                    server_service(client,recv_data.decode("utf-8"))
                # 对方调用close导致recv为空
                else:
                    client.close()
                    client_list.remove(client)


if __name__ == "__main__":
    main()
