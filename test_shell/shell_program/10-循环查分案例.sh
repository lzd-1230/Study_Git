#!/bin/bash

for ((;;))
do
# 提示信息
  echo -n "Plese input scorce:"
# 循环输入分数
  read S 
  if [ $S -lt 0 -o $S -gt 100 ]
  then 
    echo "分数要在[0,100]内"
    continue
  fi
# 将输入进行处理和判断
  I=`expr $S / 10`
  case $I in
    9 | 10)
      echo "A"
      ;;
    8)
      echo "B"
      ;;
    7 | 6)
      echo "C"
      ;;
    *)
      echo "filed"
      ;;
  esac
done
