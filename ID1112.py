#!/usr/bin/python3
import math

list_A = eval(input())
list_B = eval(input())

if (len(list_A) != len(list_B)):
    print("The length is not same")
else:
    sum_A = 0
    sum_B = 0
    sum_AB = 0

    for i in list_A:
        sum_A += i*i
    
    for i in list_B:
        sum_B += i*i
    
    if (sum_A*sum_B != 0):
        for i in range(len(list_A)):
            sum_AB += list_A[i]*list_B[i]
        
        if (sum_AB >= 0):
            print("%0.6f" %(math.sqrt((sum_AB*sum_AB)/(sum_A*sum_B))))
        else:
            print("-%0.6f" %(math.sqrt((sum_AB*sum_AB)/(sum_A*sum_B))))
    elif (sum_A == 0) and (sum_B == 0):
        print("1.000000")
    else:
        print("0.000000")