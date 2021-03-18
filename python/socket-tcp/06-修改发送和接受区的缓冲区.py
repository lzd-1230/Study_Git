import socket


def main():
    s_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    """得到缓冲区大小"""
    bsize = s_tcp.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print(f"当前发送缓冲区大小:{bsize}")
    bsize = s_tcp.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    print(f"当前接受缓冲区大小:{bsize}")

    # 设置缓冲区大小
    s_tcp.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,4096)
    s_tcp.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,4096)
    # 修改后的大小
    bsize = s_tcp.getsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF)
    print(f"当前发送缓冲区大小:{bsize}")
    bsize = s_tcp.getsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF)
    print(f"当前接受缓冲区大小:{bsize}")







if __name__ == "__main__":
    main()
