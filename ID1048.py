#!/usr/bin/python3
import math

def f(x): 
    if x == 1: return 0 
    global cnt 
    s = int(math.sqrt(x))
    for i in range(2, s + 1): 
        cnt += 1 
        if x % i == 0: return 1 
    return 2



result = []
input_list = []
try:
    while(1):
        input_list.append(int(input()))
except EOFError:
    pass
f(max(input_list))
for i in input_list:
    print(result[input_list[i]])

