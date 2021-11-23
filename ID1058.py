#!/usr/bin/python3

def cut_int(input_num):
    length = int(len(input_num)/2)
    num_lr = int(input_num[:length]) * int(input_num[length:])
    if (num_lr == 0) or (int(input_num) % num_lr != 0):
        return ("No")
    else:
        return ("Yes")

input_flag = int(input())
result = []
for i in range(input_flag):
    result.append(cut_int(input()))

for i in result:
    print(i)
