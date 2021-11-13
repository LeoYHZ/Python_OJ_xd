#!/usr/bin/python3
import ast

def same_word_list(list_1, list_2):
    same_result = []
    flag = 0
    while flag < len(list_1):
        if (list_1[flag] in list_2):
            same_result.append(list_1[flag])
            list_2.remove(list_1[flag])
            list_1.remove(list_1[flag])
        else:
            flag += 1
    return same_result


input_list = ast.literal_eval(input())
same_word = sorted(input_list[0])
for i in range(len(input_list) - 1):
    same_word = same_word_list(sorted(input_list[i + 1]), same_word)

print("\"" + "".join(same_word) + "\"")
# 将列表修改为字符串进行输出
