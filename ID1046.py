#!/usr/bin/python3
from fractions import Fraction

input_1 = input().split("/")
input_2 = input().split("/")

final_a = (int(input_1[0]) * int(input_2[1])) + (int(input_1[1]) * int(input_2[0]))
final_b = int(input_1[1]) * int(input_2[1])

if (final_a == 0):
    print("0/1")
else:
    print(Fraction(final_a, final_b))