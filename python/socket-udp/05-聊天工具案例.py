import socket

def send_msg(udp_socket,dest_ip,dest_port):
    send_data = input("请输入需要发送的内容:")
    udp_socket.sendto(send_data.encode("gbk"),(dest_ip,dest_port))


def rec_msg(udp_socket):
    data_recv = udp_socket.recvfrom(1024)
    print("%s,from %s" % (data_recv[0].decode("gbk"),str(data_recv[1])))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    udp_socket.bind(("",7780))  # 绑定端口
    # 输入目标信息
    dest_ip = input("请输入目标ip:")
    dest_port = int(input("请输入目标端口:"))
    # 循环处理
    while True:
        print("***************聊天器**************")
        print("1:发送消息")
        print("2:接受消息")
        print("0:退出程序")
        print("***************聊天器**************")

        op = input("请输入操作:")
        if op == "1":
            # 发送数据
            send_msg(udp_socket,dest_ip,dest_port)
        elif op == "2":
            # 接受并显示数据
            rec_msg(udp_socket) 
        elif op == "0":
            print("推出程序")
            break
        else:
            print("输入有误")



if __name__ == "__main__":
    main()
