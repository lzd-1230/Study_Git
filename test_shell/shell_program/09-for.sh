# !/bin/bash
# 用一系列变量当作列表
#for I in i 3 4 5 6 
# 用一个命令的结果当作列表
for I in `ls /etc`
do 
    echo $I
done
# seq命令类似于range,(首,步长,尾)
for I in `seq 1 2 12`
do 
    echo $I
done

