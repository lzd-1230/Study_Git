import socket
import re

def tackle_request(request_info):
    """解析用户的请求"""
    request_lines = request_info.splitlines()
    print(">>"*20)
    print(request_lines)
    print(">>"*20)
    # GET /index.html HTTP/1.1
    if request_lines:
        # 找到请求的文件名
        ret = re.match(r"[^/]+([^ ]*)",request_lines[0])  # 取出请求的内容
        if ret:
            file_name = ret.group(1)
            # 默认访问index页面
            if file_name == "/":
                file_name = "/index.html"
            print("***"*20)
            print(f"访问的内容是{file_name}")
            print("***"*20)
            return file_name
    return ""

def server_service(client_socket,request_info):
    # 接受客户端发送过来的请求
    # GET /index.html HTTP/1.1......
#    request_info = client_socket.recv(1024).decode("utf-8")
#    print(">>>"*50)
#    print(request_info)
#    print(">>>"*50)
    file_name = tackle_request(request_info)

    # 发送对应的数据
    try:  # 打开一个文件是一件很危险的事情
        f = open("./python-3.6.12-docs-html"+file_name,"rb")
    except:
        respond_header = "HTTP/1.1 404 NOT FOUND \r\n"
        respond_header += "\r\n"
        respond_header += "----------file not found------------"
        # 发送数据
        client_socket.send(respond_header.encode("utf-8"))
    # 准备发送数据
    else:
        html_content = f.read()
        f.close()

        respond_header = "HTTP/1.1 200 OK\r\n"  # 返回一个标准的应答
        respond_header += "Content-Length:%d\r\n" % len(html_content)
        respond_header += "\r\n"
        # 将内容发送给浏览器
        respond_all = respond_header.encode("utf-8") + html_content
        client_socket.send(respond_all)
        client_socket.send(html_content)
        # 浏览器四次挥手
        client_socket.close()
