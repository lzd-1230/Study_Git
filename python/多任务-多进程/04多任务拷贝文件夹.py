import os
import multiprocessing

def copy_file(queque,f_name,new_folder_path,old_folder_path):
    """完成文件的复制"""
    new_path = os.path.join(new_folder_path,f_name)
    origin_path = os.path.join(old_folder_path,f_name)

    origin_file = open(origin_path,"rb")
    # print(f"正在复制{origin_path}")
    # 如果要拷贝大文件,这里就换成while True
    content = origin_file.read() 
    origin_file.close()

    new_file = open(new_path,"wb")
    new_file.write(content)
    new_file.close()
    queque.put(f_name)
    # print(f"已经完成复制{f_name}")


def main():
    # 获取文件夹的名字
    old_folder = input("请输入要拷贝的文件夹的名字(当前目录下)")
    # 创建文件夹 
    new_folder_path = old_folder+"_cp"
    old_folder_path = old_folder

    if os.path.exists(new_folder_path):
        print("文件夹已经存在")
    else:
        # 创建一个新的文件夹
        os.mkdir(old_folder + "_cp")
    files_names = os.listdir(old_folder)
    # print(files_names)
    # 用进程池来复制文件
    po = multiprocessing.Pool(5)

    queque = multiprocessing.Manager().Queue()
    # 向进程池里面添加 copy任务
    for f_name in files_names:
        po.apply_async(copy_file,args = (queque,f_name,new_folder_path,old_folder_path))
    po.close() 
    # po.join()
    curent_num = 0
    all_file_num = len(files_names)
    while True:
        return_from_course = queque.get()
        curent_num += 1 
        print("\r当前复制进度为%.2f%%" % (curent_num*100/all_file_num),end = "")
        if curent_num == all_file_num:
            print("")
            break

    print("------已经完成了所有文件的复制-------") 


if __name__ == "__main__":
    main()
