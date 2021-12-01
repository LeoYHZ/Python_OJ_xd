#!/usr/bin/python3

num_N = int(input())
num_list_P = list(map(int, input().split(" ")[:-1]))
num_Q = int(input())
num_test = []
for i in range(num_Q):
    num_test.append(int(input()))

for i in num_test:
    num_flag = 0
    num_start = 0
    for k in range(40):
        for j in range(num_start, num_N):
            if (i & num_list_P[j] == num_list_P[j]):
                num_flag = num_flag | num_list_P[j]
                num_start = j + 1
                break
        if (num_start == 0):
            break
    if (num_flag == i):
        print("YES")
    else:
        print("NO")
