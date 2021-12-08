#!/usr/bin/python3
def sun_list(input_list, num_flag):
    global num_final
    output_list = []
    for i in input_list:
        if isinstance(i, list):
            output_list += i
        elif isinstance(i, int):
            num_final += num_flag
    return output_list

input_data = eval(input())
num_final = 0
num_flag = 1

while (any(isinstance(i, list) for i in input_data)):
    input_data = sun_list(input_data, num_flag)
    num_flag += 1

for i in input_data:
    if isinstance(i, int):
        num_final += num_flag

print(num_final)