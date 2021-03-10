# !/bin/bash
A=$(expr 3 + 5 \* 4)
echo $A

A=12
B=12
test $A -eq $B
echo "测试的结果为:"$?
