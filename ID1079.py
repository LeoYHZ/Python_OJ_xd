#!/usr/bin/python3
import json

input_data = json.loads(input())

print(",".join(list(input_data[0].keys())))
for i in range(len(input_data)):
    print(",".join(list(input_data[i].values())))
