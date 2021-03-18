import re 
names = ["name1","_name","2_name","__name__","_name!"]

for name in names:
    ret = re.match(r"^[a-zA-Z_]+\w*$",name)
    if ret:
        print(f"{name}是满足要求的")
    else:
        print(f"{name}是不满足要求的")

