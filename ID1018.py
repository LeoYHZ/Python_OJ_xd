#!/usr/bin/python3
input_list = []

while(1):
    try:
        input_list.append(int(input()))
    except EOFError:
        break

final_result = 1

for i in range(len(input_list)):
    result = 0
    for j in range(i, len(input_list)):
        if (input_list[i] == input_list[j]):
            result += 1
    if (result > final_result):
        final_result = result

print(final_result)