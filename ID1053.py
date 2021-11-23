#!/usr/bin/python3
input_list = input().split(" ")
num_N = int(input_list[0])
for i in range(int((num_N + 1)/2)):
    print(input_list[1]*num_N)
