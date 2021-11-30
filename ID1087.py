#!/usr/bin/python3
num_list = []

try:
    while(1):
        num_list.append(input())
except EOFError:
    pass

def num_th(i):
    if (i[-1] == "1"):
        print("{}st".format(i))
    elif (i[-1] == "2"):
        print("{}nd".format(i))
    elif (i[-1] == "3"):
        print("{}rd".format(i))
    else:
        print("{}th".format(i))

for i in num_list:
    if (len(i) > 1):
        if (i[-2] == "1"):
            print("{}th".format(i))
        else:
            num_th(i)
    else:
        num_th(i)
