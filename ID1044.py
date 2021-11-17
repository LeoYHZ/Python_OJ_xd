#!/usr/bin/python3

input_num = int(input())
input_list = []
for i in range(input_num):
    input_list.append(input())

for i in range(input_num):
    output_num = 0
    for j in range(4):
        output_num += (ord(input_list[i][j]) + ord(input_list[i][j+5])) * (256 ** (3-j))
    print(output_num)
