#!/usr/bin/python3
from collections import Counter

num_N = int(input())
num_time = list(map(int, input().split()))

num_time_dic = Counter(num_time)
keylist = sorted(num_time_dic.keys())
for i in keylist:
    print("{}:{}".format(i,num_time_dic[i]))
