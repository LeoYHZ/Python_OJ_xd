#!/usr/bin/python3 

num_N, num_NA, num_NB = map(int, input().split(" "))

NA_list = input().split(" ")
NB_list = input().split(" ")

NA_list = NA_list * (int(num_N/num_NA)) + NA_list[0:num_N%num_NA]
NB_list = NB_list * (int(num_N/num_NB)) + NB_list[0:num_N%num_NB]

result = 0

for i in range(num_N):
    flag = int(NA_list[i]) + (5*int(NB_list[i]))
    if (flag in [0, 6, 12, 18, 24]):
        pass
    elif (flag in [1, 4, 7, 9, 10, 13, 15, 16, 22, 23]):
        result += 1
    else:
        result -= 1

print("{} {}".format(result, -1 * result))