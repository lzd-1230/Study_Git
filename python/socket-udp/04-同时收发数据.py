import socket
'''
套接字是可以同时收发数据
'''
def main():
	#创建套接字
    s_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定本地端口
    local_addr = ("",7786)
    s_udp.bind(local_addr)
    
    dest_ip = input("请输入对方的ip:")
    try:
        dest_port = int(input("请输入对方的port:"))
        send = input("请输入要发送的内容:\n")
        #发送数据
        s_udp.sendto(send.encode("gbk"),(dest_ip,dest_port))
        # 接受回来的数据
        recv_data = s_udp.recvfrom(1024)
        # 打印数据
        rec_data = recv_data[0]
        rec_addr = recv_data[1]
        print("%s,from%s"%(rec_data.decode("gbk"),rec_addr))
        # 关闭
        s_udp.close()
        print("------finish---------")
    except:
        print("输入有误")

if __name__ == "__main__":
	main()
