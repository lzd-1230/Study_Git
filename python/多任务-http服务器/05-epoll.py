import socket
import select
import time 
from httpfun.HttpService import * 

def main():
    # 创建套接字
    s_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s_tcp.bind(("",7890))
    s_tcp.listen(128)
    s_tcp.setblocking(False)
    # 创建一个select对象 
    epl = select.epoll()
    # 将tcp监听套接字注册
    epl.register(s_tcp.fileno(),select.EPOLLIN)
    # 创建fd-套接字的字典
    socket_dict = dict()
    # 开始循环检测数据是否到来
    while True:
        fd_event_list = epl.poll()  # 返回一个元组(fd,event)
        for fd,event in fd_event_list:
            # 判断event到底是有客户端连接还是已连接的客户端发数据来了
            if fd == s_tcp.fileno():
                s_client,addr_client = s_tcp.accept()
                epl.register(s_client.fileno(),select.EPOLLIN)
                socket_dict[s_client.fileno()] = s_client
            # 如果fd不是监听套接字的
            elif event == select.EPOLLIN:
                # 通过fd找到套接字
                cur_client = socket_dict[fd]
                recv_data = cur_client.recv(1024)
                # 假如是close
                if not recv_data:
                    cur_client.close()  # 关闭客服套接字
                    del socket_dict[fd]  # 从字典中删除
                    epl.unregister(fd)  # 从epoll内存中删除
                else:
                    server_service(cur_client,recv_data)







if __name__ == "__main__":
    main()
