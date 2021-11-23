#!/usr/bin/python3
input_list = []

while(1):
    try:
        input_list.append(input())
    except EOFError:
        break

Class = input_list[0].split(",")

if ("target" not in Class):
    print("File is not OK!")
else:
    target_flag = Class.index("target")
    for i in range(1, len(input_list)):
        if (input_list[i].split(",")[target_flag] == "1"):
            print(input_list[i])
