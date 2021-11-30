#!/usr/bin/python3
import json
import math

def judge(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return True

for i in json.loads(input()):
    if(judge(i["Value"])):
        print(i["ID"])