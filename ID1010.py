#!/usr/bin/python3 
input_num = int(input())
sum_num = 0
flag = 0
while (flag < input_num):
    sum_num += int(input())
    flag += 1

print("%d %.5f" %(sum_num, sum_num/input_num))
