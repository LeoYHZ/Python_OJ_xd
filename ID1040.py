#!/usr/bin/python3
input_data = input().split(" ")
num_N = int(input_data[0])
num_K = int(input_data[1])

num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

num_result = []
while(num_N / num_K > 0):
    num_result.insert(0, num_list[num_N % num_K])
    # 从list的开头插入数据
    num_N = num_N // num_K

print("".join(num_result))