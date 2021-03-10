#!/bin/bash
grep_user()
{
  I=`grep "lzd" /etc/passwd | wc -l`
  echo "函数中打印"$I
  return $I
}

echo -n "请输入用户名:"
read USER
grep_user $USER
ret=$?
echo ret 

if [ $ret -eq 1 ]
then
  echo "用户$USER存在"
else
  echo "用户$USER不存在"
fi
