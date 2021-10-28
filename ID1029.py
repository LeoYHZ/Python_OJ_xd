#!/usr/bin/python3 
import json
input_list = []

# json结构相当于一个只含有一个元素的list，其内部仅有一个dict。

while(1):
    try:
        input_list.append(input())
    except EOFError:
        break

Class = input_list[0].split(",")

output_result = []

for i in range(len(input_list) - 1):
    data_insert = dict(sorted(zip(Class, input_list[i + 1].split(","))))
    output_result.append(data_insert)

# 使用zip函数对对两组数据进行组合，然后通过对Class的sorted给出顺序结果，最终加入list即可。
# 注意python3中的zip函数输出无法直接打印

print(json.dumps(output_result, indent=4))

# 添加intent进行输出的缩进