#!/usr/bin/python3 
input_num = int(input())
count_4 = 0
count_7 = 0

while (input_num % 4 == 0):
    count_4 += 1
    input_num = input_num//4
# 注意/于//的区别，此处使用//可以避免使用/时造成的数据溢出。
while (input_num % 7 == 0):
    count_7 += 1
    input_num = input_num//7

print("%d %d" %(count_4, count_7))
