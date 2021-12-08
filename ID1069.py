#!/usr/bin/python3
import math

num_P = int(input())
num_length = int(math.log10(2) * num_P) + 1
print(num_length)

num_str = str((2 ** num_P) - 1)
num_first = num_str[0]
if (num_length < 500):
    num_str = "0"*(500 - num_length) + num_str

num_str = num_str[-500:]

for i in range(10):
    print(num_str[i*50:(i+1)*50])

print(num_first)