#!/usr/bin/python3

num_weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
num_judge = ["1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"]
input_list = []
flag_all = True

input_num = int(input())
for i in range(input_num):
    input_list.append(input())

for i in range(input_num):
    flag = True
    sum_data = 0

    try:
        num_ID = int(input_list[i][:-1])
    except ValueError:
        print(input_list[i])
        flag = False
        flag_all = False

    if (flag):
        for j in range(17):
            sum_data += int(input_list[i][j]) * num_weight[j]
        if (num_judge[sum_data % 11] != input_list[i][-1]):
            flag_all = False
            print(input_list[i])

if (flag_all):
    print("All passed")