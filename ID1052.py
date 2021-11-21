#!/usr/bin/python3

input_num = int(input())
num_list = list(map(int, input().split()))

num_inversion = 0
# for i in range(input_num - 1):
#     for j in range(i + 1,input_num):
#         if (num_list[i] > num_list[j]):
#             num_inversion += 1

flag_list = [0]*11
for i in range(input_num):
    flag_list[num_list[i]] = flag_list[num_list[i]] + 1
    num_inversion += sum(flag_list[(num_list[i] + 1):])

print(num_inversion)