#!/usr/bin/python3 
input_num = int(input())
if input_num >= 0:
    if input_num < 60:
        print("F")
    elif input_num < 70:
        print("D")
    elif input_num < 80:
        print("C")
    elif input_num < 90:
        print("B")
    elif input_num <= 100:
        print("A")
    else:
        print("Error!")
else:
    print("Error!")