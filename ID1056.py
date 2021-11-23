#!/usr/bin/python3
import math

def Prime_num(input_num):
    result = 1
    for i in range(2,int(math.sqrt(input_num) + 2)):
        if (input_num%i == 0):
            result = 0
            break
    return result

def Sum_eve(input_num):
    result = 0
    while (input_num >= 10):
        result += ((input_num % 10) ** 2)
        input_num = int(input_num / 10)
    result += (input_num ** 2)
    return result

def happy(input_num):
    global result
    global intra_num
    prime_original = Prime_num(input_num)
    sum_list = []
    flag = 0
    while(Sum_eve(input_num) not in sum_list):
        flag += 1
        input_num = Sum_eve(input_num)
        if (input_num == 1):
            intra_num += sum_list
            return (flag * (2 ** prime_original))
        sum_list.append(input_num)
    return 0
    
A, B = map(int, input().split(" "))
result_num = {}
intra_num = []

for i in range(A, B + 1):
    result = happy(i)
    if (result != 0):
        result_num.update({i: result})

if( len(result_num) == 0):
    print("SAD")
else:
    for i in result_num:
        if (i not in intra_num):
            print("{} {}".format(i, result_num[i]))
