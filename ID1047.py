#!/usr/bin/python3
import math

def prime_num( num ):
    flag = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num%i == 0):
            flag = False
            break
    return flag

def count(num_n):
    cnt = 0
    for i in range(3, num_n + 1, 2):
        if (prime_num(i)):
            cnt += (i - 2)
        else:
            for j in range(3,i):
                cnt += 1
                if (i % j == 0):
                    break
    return cnt + max(int(num_n / 2), 1) - 1

input_list = []
try:
    while(1):
        input_list.append(input())
except EOFError:
    pass

for i in range(len(input_list)):
    print(count(int(input_list[i])))
