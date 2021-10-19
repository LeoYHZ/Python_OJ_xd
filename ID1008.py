#!/usr/bin/python3 
input_num_0 = int(input())
input_num_1 = int(input())

while (input_num_1 > 0):
    flag = input_num_0 % input_num_1
    input_num_0 = input_num_1
    input_num_1 = flag

print(input_num_0)