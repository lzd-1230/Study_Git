import re 
while True:
    emil_id = input("请输入一个邮箱:")

    ret = re.match(r"^[a-zA-Z_]{4,20}@163\.com$",emil_id)
    if ret:
        print(f"{emil_id}是满足要求的")
    else:
        print(f"{emil_id}是不满足要求的")

