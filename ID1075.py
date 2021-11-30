#!/usr/bin/python3
import json
input_list = []
result = []

try:
    while(1):
        input_list.append(input())
except EOFError:
    pass

Class = input_list[0].split(",")

try:
    flag = Class.index("target")
    for i in range(1, len(input_list)):
        num_list = input_list[i].split(",")
        if (num_list[flag] == "1"):
            result.append(dict(zip(Class, num_list)))
    print(json.dumps(result, sort_keys=False, indent=4))
except ValueError:
    print("File is not OK!")