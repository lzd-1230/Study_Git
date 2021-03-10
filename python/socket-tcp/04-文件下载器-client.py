import socket

def main():
    # 创建套接字
    s_download = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 获取dest_ip dest_port
    #dest_ip = input("请输入目标ip:")
    dest_ip = "10.0.0.8"
    dest_port = int(input("请输入目标端口:"))
    dest_addr = (dest_ip,dest_port)
    # 链接服务器
    s_download.connect(dest_addr)
    # 获取下载文件的名字
    file_name = input("请输入要下载的文件名:")
    # 将文件名发送到服务器
    s_download.send(file_name.encode("gbk"))
    # 接受文件中的数据
    file_recv = s_download.recv(1024*1024)
    # 保存接受到的数据到文件中
    if file_recv:
        with open("download_"+file_name,"w") as f:
            f.write(file_recv.decode("gbk"))
    # 关闭套接字
    s_download.close()
    

if __name__ == "__main__":
    main()
