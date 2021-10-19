#!/usr/bin/python3 
input_num = input()
try:
    result = int(input_num.split(" ")[0]) + int(input_num.split(" ")[1])
except ValueError:
    print ("Input format wrong!")
print(result)
