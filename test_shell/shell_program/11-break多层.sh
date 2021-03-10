#!/bin/bash

for ((I=0; I <=3; I++))
do
  for((J=1; J<=4; J++))
  do
    if [ $I -ge 2 ]
    then 
      break 2 
    fi
    echo "$I - $J" 
  done
  
done
