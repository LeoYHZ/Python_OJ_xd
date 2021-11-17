#!/usr/bin/python3
input_num = input()
input_list = input().split(" ")

num_0 = 0
num_5 = 0
for i in range(len(input_list)):
    if (input_list[i] == "0"):
        num_0 += 1
    else:
        num_5 += 1

if (num_0 == 0):
    print("-1")
elif (num_5 < 9):
    print("0")
else:
    print("5" * 9 * (num_5 // 9) + "0" * num_0)
