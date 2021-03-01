import socket
import threading


def send_msg(udp_socket,dest_ip,dest_port):
    while True:
        send_data = input("请输入需要发送的内容:\n")
        udp_socket.sendto(send_data.encode("gbk"),(dest_ip,dest_port))


def rec_msg(udp_socket):
    while True:
        data_recv = udp_socket.recvfrom(1024)
        print("*************对方发来***************")
        print("%s,from %s" % (data_recv[0].decode("gbk"),str(data_recv[1])))
        print("**************************")
        print("请输入需要发送的内容:")


class MyThread_send(threading.Thread):
    def __init__(self,udp_socket,dest_ip,dest_port):
        threading.Thread.__init__(self)
        self.udp_socket = udp_socket
        self.dest_ip = dest_ip
        self.dest_port = dest_port


    def run(self):
        send_msg(self.udp_socket,self.dest_ip,self.dest_port)


class MyThread_recv(threading.Thread):
    def __init__(self,udp_socket):
        threading.Thread.__init__(self)
        self.udp_socket = udp_socket


    def run(self):
        rec_msg(self.udp_socket) 


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7780))  # 绑定端口
    # 输入目标信息
    dest_ip = "10.0.0.37"
    dest_port = 8080
    # 创建进程对象
    t_recv = MyThread_recv(udp_socket)
    t_send = MyThread_send(udp_socket,dest_ip,dest_port)

    print("***************聊天器**************")
    # 打开接受和发送进程
    t_recv.start()
    t_send.start()

if __name__ == "__main__":
    main()
