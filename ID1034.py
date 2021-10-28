#!/usr/bin/python3
import math
input_num = int(input())

def prime_num( num ):
    # 质数的判断
    flag = True
    for i in range(2, int(math.sqrt(num)) + 1):
        # 不用遍历所有，小于num的开方即可
        if (num%i == 0):
            flag = False
            break
    return flag

prime_num_list = []
while(1):
    if (prime_num(input_num)):
        prime_num_list.append(input_num)
    input_num -= 1
    if ((len(prime_num_list) == 2) or (input_num == 2)):
        break

print(prime_num_list[::-1])