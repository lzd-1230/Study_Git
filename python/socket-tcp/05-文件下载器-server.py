import socket


def send_file_2_client(client_socket,client_addr):
    # 接受客户端发送过来的文件名
    file_name = client_socket.recv(1024).decode("utf-8")
    print("客户端%s需要下载的文件名是%s" % (str(client_addr),file_name)) 
    
    file_content = ""

    # 打开文件读入数据并发送
    try:
        f = open(file_name,"r")
        file_content = f.read()
        f.close()
    except:
        print("没有文件%s" % file_name)

    if file_content:
        client_socket.send(file_content.encode("gbk"))

def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    # 绑定本地ip
    tcp_server.bind(("",7789))

    # 设置为被动模式(listen)
    tcp_server.listen(128)  # 128代表
    
    while True:
        # 等待连接(accept),这里会堵塞直到有第一个客户端连接
        print("----waiting for connect----")
        client_socket,client_addr = tcp_server.accept()
        print("----finish connect----")
        print(client_addr)

        # 发送文件给客户端
        send_file_2_client(client_socket,client_addr)  # 发送套接字
        # 关闭套接字
        client_socket.close()
    tcp_server.close()
if __name__ == "__main__":
    main()
