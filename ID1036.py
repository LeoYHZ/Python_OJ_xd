#!/usr/bin/python3
input_data = input()
offset = int(input())

result = ""

for i in range(len(input_data)):
    if (ord(input_data[i]) >= 65) and (ord(input_data[i]) <= 90):
        if ((ord(input_data[i]) + (offset % 26)) > 90):
            result += chr(65 - 1 + ((ord(input_data[i]) + (offset % 26)) % 90))
        else:
            result += chr(ord(input_data[i]) + (offset % 26))
    elif (ord(input_data[i]) >= 97) and (ord(input_data[i]) <= 122):
        if ((ord(input_data[i]) + (offset % 26)) > 122):
            result += chr(97 - 1 + ((ord(input_data[i]) + (offset % 26)) % 122))
        else:
            result += chr(ord(input_data[i]) + (offset % 26))
    else:
        result += input_data[i]
print(result)