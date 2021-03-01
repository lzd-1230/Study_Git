import socket

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定本地端口
    local_addr = ("",7786)
    udp_socket.bind(local_addr)
    # 接受数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # 打印数据
        rec_data = recv_data[0]
        rec_addr = recv_data[1]
        print("%s,from%s"%(rec_data.decode("gbk"),rec_addr))
        # 关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
