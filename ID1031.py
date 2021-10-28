#!/usr/bin/python3
flag = 0
input_time = 3
while(flag < input_time):
    name = input()
    passwd = input()
    if ((name == "Pile") and (passwd == "MAKIKAWAYI")):
        print("SUCCESS")
        flag = input_time + 1
    flag += 1

if(flag == input_time):
    print("FAILED")