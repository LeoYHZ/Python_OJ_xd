#!/usr/bin/python3 
input_data = input()

if input_data[-1] in ["R", "r"]:
    print("%dD" %(int(input_data[0:-1])/6))
elif input_data[-1] in ["D", "d"]:
    print("%dR" %(int(input_data[0:-1])*6))
else:
    print("Error!")
