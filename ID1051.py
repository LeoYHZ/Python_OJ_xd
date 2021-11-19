#!/usr/bin/python3

num_N = int(input())
num_time = list(map(int, input().split()))
num_time.sort()

## model 1
flag = 0
num_list = []
while (flag < num_N):
    time_now = num_time[flag]
    num_now = 1
    while ((flag + num_now) < num_N):
        if (num_time[flag + num_now] == time_now):
            num_now += 1
        else:
            break
    print("{}:{}".format(num_time[flag], num_now))
    flag = flag + num_now

## model 2
# num_list = {}
# for i in range(num_N):
#     if num_time[i] not in num_list:
#         num_list[num_time[i]] = 1
#     else :
#         num_list[num_time[i]] = num_list[num_time[i]] + 1
# for name in num_list:
#     print("{}:{}".format(name,num_list[name]))