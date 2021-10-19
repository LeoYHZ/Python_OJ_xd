#!/usr/bin/python3 
input_num = int(input())
sum_num = 0
flag = 1
while (flag <= input_num):
    factorial = 1
    for i in range(1,flag + 1):
       factorial = factorial*i
    sum_num += factorial
    flag += 1

print("%d" %(sum_num))
