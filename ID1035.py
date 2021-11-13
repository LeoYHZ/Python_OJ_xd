#!/usr/bin/python3
import random

def compute_pi(num, seed):
    random.seed(seed)
    num_in_circle = 0
    for i in range(num):
        x = random.random()
        y = random.random()
        if ((x*x + y*y) <= 1) :
            num_in_circle += 1
    return 4*num_in_circle / num

input_num = int(input())
seed_num = int(input())
print("%.6f" %compute_pi(input_num, seed_num))