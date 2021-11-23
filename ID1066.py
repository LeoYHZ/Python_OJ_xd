#!/usr/bin/python3

input_num_1 = int(input())
input_list_1 = []
for i in range(input_num_1):
    input_list_1.append(int(input()))

input_num_2 = int(input())
input_list_2 = []
for i in range(input_num_2):
    input_list_2.append(int(input()))

input_list_1.sort()

for i in input_list_2:
    print(input_list_1[i])