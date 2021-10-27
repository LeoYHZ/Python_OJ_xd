#!/usr/bin/python3 
input_list = []

while(1):
    try:
        input_list.append(input())
    except EOFError:
        break

for i in range(len(input_list)):
    # print(input_list[i])
    print(input_list[i].replace(",","\t") + "\t")
