#!/usr/bin/python3

def flatten_deep(num_list):
    num_list_new = []
    for i in num_list:
        if isinstance(i, (list,tuple)):
            num_list_new += flatten_deep(i)
        else:
            num_list_new.append(i)
    return num_list_new

input_list = []
try:
    while(1):
        input_list.append(eval(input()))
except EOFError:
    pass

for i in input_list:
    print(flatten_deep(i))
