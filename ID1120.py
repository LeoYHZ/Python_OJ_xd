#!/usr/bin/python3

num_A,num_B = map(int, input().split())

num_A_2 = bin(num_A)[2:]
num_A_2 = ("0" * (num_B - len(num_A_2))) + num_A_2

num_A_3 = ""
for i in num_A_2:
    if (i == "0"):
        num_A_3 += "1"
    else:
        num_A_3 += "0"

print(int(num_A_3,2))