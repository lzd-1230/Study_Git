# !/bin/bash
# 假如没有输入参数
if [ $# -ne 1 ]
then 
    echo "要输入一个参数为文件名"
    exit
fi
# 加入文件不存在
if ! [ -e $1 ]
then
    echo "$1 not exist"
    exit
fi

if [ -d $1 ]
then 
    echo "$1 is a directory"
else
    echo "$1 is not a directory"
fi
