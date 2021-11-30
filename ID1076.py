#!/usr/bin/python3
import json

num_N, num_M = map(int, input().split(" "))
row_list = []

def sum_boom(matrix, i, j, num_N, num_M):
    sum_result = 0
    # print(matrix)
    for ii in range(max(0, i-1), min(num_N, i+2)):
        for jj in range(max(0, j-1), min(num_M, j+2)):
            if(matrix[ii][jj] == "*"):
                sum_result += 1
    return sum_result

for i in range(num_N):
    row_list.append(list(input()))

for i in range(num_N):
    for j in range(num_M):
        if (row_list[i][j] != "*"):
            row_list[i][j] = sum_boom(row_list, i , j, num_N, num_M)

for i in range(num_N):
    print("".join(map(str, row_list[i])))
