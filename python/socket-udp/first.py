import socket

def main():
	#创建套接字
    s_udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    #发送数据
    s_udp.sendto(b"hahahah-----test------",("192.168.1.100",8080))

    # 关闭
    s_udp.close()
    print("------finish---------")

if __name__ == "__main__":
	main()
