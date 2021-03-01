import socket

def main():
	#创建套接字
    s_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while(True):
        send = input("请输入要发送的内容:\n")
        if(send == "exit"):
            break
        #发送数据
        s_udp.sendto(send.encode("gbk"),("192.168.1.100",8080))

    # 关闭
    s_udp.close()
    print("------finish---------")

if __name__ == "__main__":
	main()
