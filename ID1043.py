#!/usr/bin/python3

input_num = int(input())
input_list = []

for i in range(input_num):
    input_list.append(input())

for i in range(input_num):
    if (len(input_list[i]) == 11):
        print("6" + input_list[i][-5:])
    else:
        print("Halation - I can't join it!")