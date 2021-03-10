# !/bin/bash

echo "请输入(yes/no)"

read Y
case $Y in
    yes| Y)
      echo "yes"
      ;;
    no)
        echo "no"
        ;;
    *)
      echo "wrong"
      ;;
esac
