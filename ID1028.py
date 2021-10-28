#!/usr/bin/python3 
input_num = int(input())
flag = (input_num >= 0)
input_num = abs(input_num)

output_num = ""
output_0x_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

while (input_num > 0):
    output_num += output_0x_list[input_num % 16]
    input_num = input_num // 16
if (flag):
    print("0x" + output_num[::-1])
else:
    print("-0x" + output_num[::-1])
