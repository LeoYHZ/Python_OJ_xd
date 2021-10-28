#!/usr/bin/python3 
input_data = input()[1:-1].split(", ")
input_num = input()

for i in range(len(input_data)):
    if (input_num == input_data[i].split(": ")[0][1:-1]):
        print(input_data[i].split(": ")[1][1:-1])