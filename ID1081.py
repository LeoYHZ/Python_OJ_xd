#!/usr/bin/python3
import json

input_data = json.loads(input())
num_A, num_B = map(int, input().split(" "))

result_ID = []

for i in range(len(input_data)):
    if (input_data[i]["Value"] >= num_A) and (input_data[i]["Value"] <= num_B):
        result_ID.append(input_data[i]["ID"])

for i in result_ID:
    print(i)