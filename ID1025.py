#!/usr/bin/python3 
input_list = []

while(1):
    try:
        input_list.append(int(input()))
    except EOFError:
        break

sum_result = 0.0
for i in range(len(input_list)):
    sum_result = sum_result + input_list[i]

aver_result = sum_result/(len(input_list))

sum_result = 0.0
for i in range(len(input_list)):
    sum_result = sum_result + ((input_list[i] - aver_result) ** 2)

Standard_Deviation = (sum_result/(len(input_list) - 1)) ** 0.5
# 本题求解的是样本标准差，所以要除以n-1，对于总体标准差，是除以n。

print("dev = {:.2}.".format(Standard_Deviation))