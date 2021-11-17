#!/usr/bin/python3
input_data = input().split(" ")
num_n = int(input_data[0])
num_a = int(input_data[1])

def num_na(num_1, num_2):
    num_na = 0
    while(num_2 > 0):
        num_na += num_1 * (10 ** (num_2 - 1))
        num_2 -=1
    return num_na

result = 0
# flag = num_n
# while(flag > 0):
#     result += flag * num_a * (10 ** (num_n - flag))
#     flag -= 1

num_max = num_na(num_a, num_n)

for i in range(num_n):
    result += num_max
    num_max = num_max // 10

print(result)
