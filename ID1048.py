#!/usr/bin/python3
import math

def f(x):
    global cnt
    for i in range(3,x):
        sum_flag = cnt[-1]
        s = int(math.sqrt(i + 1))
        for j in range(2, s + 1):
            sum_flag += 1
            if (i+1) % j == 0:
                break
        cnt.append(sum_flag)


cnt = [0, 0, 0]
input_list = []
try:
    while(1):
        input_list.append(int(input()))
except EOFError:
    pass
f(max(input_list))
for i in input_list:
    print(cnt[i - 1])
