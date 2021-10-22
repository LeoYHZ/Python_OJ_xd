#!/usr/bin/python3 
input_data = input()
import math

def prime_num( num ):
    # 质数的判断
    flag = True
    for i in range(2, int(math.sqrt(num)) + 1):
        # 不用遍历所有，小于num的开方即可
        if (num%i == 0):
            flag = False
            break
    print(flag)

try:
    prime_num(int(input_data))
except:
    print('invalid')
