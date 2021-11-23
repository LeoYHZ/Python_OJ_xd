#!/usr/bin/python3

input_list = []
num_list = []
try:
    for line in iter(input, ""):
        input_list.append(int(line))
except EOFError:
    pass

for i in input_list:
    num_0 = 1
    while ((2 ** num_0) <= (i + 2)):
        num_0 += 1
    if (num_0 > 24):
        print(str(256 - (2 ** (num_0 - 24))) + ".0.0.0")
    elif (num_0 > 16):
        print("255." + str(256 - (2 ** (num_0 - 16))) + ".0.0")
    elif (num_0 > 8):
        print("255.255." + str(256 - (2 ** (num_0 - 8))) + ".0")
    else:
        print("255.255.255." + str(256 - (2 ** num_0)))
