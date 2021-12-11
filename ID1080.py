#!/usr/bin/python3
import json
input_data = ""

try:
    while(1):
        input_data += input()
except EOFError:
    pass

input_data = json.loads(input_data)

print(",".join(list(input_data[0].keys())))
for i in range(len(input_data)):
    print(",".join(list(input_data[i].values())))
