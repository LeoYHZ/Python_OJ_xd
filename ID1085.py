#!/usr/bin/python3
from enum import Flag
import re

color_list = []

def F2rgb(color_F):
    return str(int(color_F, 16))

def rgb2F(color_rgb):
    return hex(color_rgb)[2:].upper().zfill(2)
    # 对于小于2位的字符串，对其前方补零处理

try:
    while(1):
        input_data = input()
        if (input_data[0] == "#"):
            color_list.append(True)
            color_list.append(list(re.findall(r".{2}", input_data[1:])))
            # 以两个为间隔输出所有的数据
        else:
            color_list.append(False)
            color_list.append(list(map(int, input_data[4:-1].split(", "))))
except EOFError:
    pass

num_flag = 0
while (num_flag < len(color_list)):
    if (color_list[num_flag]):
        print("rgb(" + ", ".join(list(map(F2rgb, color_list[num_flag + 1]))) + ")")
        # 使用map进行方法映射
    else:
        print("#" + "".join(list(map(rgb2F, color_list[num_flag + 1]))))
    num_flag += 2


