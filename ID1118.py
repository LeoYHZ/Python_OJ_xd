#!/usr/bin/python3

def sun_list(input_list):
    output_list = []
    for i in input_list:
        if isinstance(i, list):
            output_list += i
    return output_list

input_data = eval(input())
input_num = int(input())
num_num = 0

for i in range(input_num - 1):
    input_data = sun_list(input_data)

for i in input_data:
    if isinstance(i, int):
        num_num += 1

print(num_num)