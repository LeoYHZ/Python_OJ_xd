#!/usr/bin/python3

num_M, num_N, num_A, num_B, num_O = map(int, input().split())
input_list = []
num_O = str(num_O).zfill(3)

for i in range(num_M):
    input_list.append(list(map(int, input().split())))

for i in range(num_M):
    for j in range(num_N):
        num_flag = input_list[i][j]
        if (num_flag>= num_A) and (num_flag <= num_B):
            input_list[i][j] = num_O
        else:
            input_list[i][j] = str(num_flag).zfill(3)

for i in range(num_M):
    print(" ".join(input_list[i]))
