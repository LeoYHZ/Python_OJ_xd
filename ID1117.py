#!/usr/bin/python3

def flag_num(num_N, flag):
    global final_num
    if (num_N == 2):
        final_num += result_2[flag]
    elif (flag > (2 ** (num_N - 1)) - 1 ):
        final_num += "1"
        flag = (2 ** num_N) - 1 - flag
    else:
        final_num += "0"
    return flag

num_N, num_K = map(int, input().split())

result_2 = ["00", "01", "11", "10"]
final_num = ""

if (num_N == 1):
    print(num_K)
else:
    for i in range(num_N - 1):
        num_K = flag_num(num_N - i, num_K)
    print(final_num)