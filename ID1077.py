#!/usr/bin/python3
import re

# inpout_1
# pattern = re.compile(r'[A-Za-z]+')   # 查找单词
# input_list = pattern.findall(input())

# input_2
input_list = input().split()



# output_1
print(" ".join(input_list[::-1]))

# output_2
# input_list.reverse()
# print(" ".join(input_list))
