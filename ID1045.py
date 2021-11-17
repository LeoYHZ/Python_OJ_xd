#!/usr/bin/python3
import re

input_data = input()

sub_obj_27 = re.sub(r'[6]{10,}', "27", input_data)
sub_obj_9 = re.sub(r'[6]{4,9}', "9", sub_obj_27)

print(sub_obj_9)
