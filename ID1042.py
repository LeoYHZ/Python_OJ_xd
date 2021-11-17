#!/usr/bin/python3

row_num = int((int(input()) + 1)/2)

for i in range(row_num):
    print(" " * (row_num - i - 1) + "*" * (2*i + 1) + " " * (row_num - i - 1) )
