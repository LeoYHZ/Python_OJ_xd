#!/usr/bin/python3 
input_num = int(input())
import math

def prime_num( num ):
    flag = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num%i == 0):
            flag = False
            break
    return flag

final_result = 0
for i in range(2, input_num//2 + 1):
    if (prime_num(i) and prime_num(input_num - i)):
        result = i*(input_num - i)
        if (result > final_result):
            final_result = result

print(result)