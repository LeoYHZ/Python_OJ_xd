#!/usr/bin/python3
import math

def prime_num( num ):
    flag = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num%i == 0):
            flag = False
            break
    return flag

num_N = int(input())

for i in range(2,5000):
    if (prime_num(i) and (num_N % i == 0)):
        print(int(num_N/i))
        break
