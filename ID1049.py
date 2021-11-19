#!/usr/bin/python3
import re
from typing import Text

def replace_passwd(str):
    numDict = {'1':'@','0':'%','l':'L','O':'o'}
    return numDict[str.group()]

input_num = int(input())
change_list = []
for i in range(input_num):
    input_data = input()
    input_data_passwd = input_data.split(" ")[1]
    if (re.findall("[1 0 l O]", input_data_passwd)):
        final_data = input_data.split(" ")[0] + " " + re.sub("[1 0 l O]", replace_passwd, input_data_passwd)
        change_list.append(final_data)

if (len(change_list) > 0):
    print(len(change_list))
    for i in (change_list):
        print(i)
elif (input_num > 1):
    print("There are " + str(input_num) + " accounts and no account is modified")
else:
    print("There is 1 account and no account is modified")
