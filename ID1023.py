#!/usr/bin/python3
input_len = int(input())
input_list = []
flag = False

for i in range(input_len):
    input_list.append(int(input()))


for i in range(len(input_list)):
    if (flag):
        break
    for j in range(i+1, len(input_list)):
        if (input_list[i] == input_list[j]):
            flag = True
            repeat_num = j + 1
            break

print(flag)
if(flag):
    print(repeat_num)