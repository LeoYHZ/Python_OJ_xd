#!/usr/bin/python3
input_num = []
for i in range(int(input())):
    input_num.append(int(input()))

Fibonacci = [1,1]
for i in range(2, max(input_num) + 1):
    Fibonacci.append(Fibonacci[i - 1] + Fibonacci[i - 2])

for i in range(len(input_num)):
    print(Fibonacci[input_num[i]])
