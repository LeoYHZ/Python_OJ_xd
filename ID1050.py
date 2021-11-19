#!/usr/bin/python3

num_m = int(input())
num_ci = list(map(int, input().split(" ")))
num_LR = list(map(int, input().split(" ")))

sum_num_ci = [num_ci[0]]
for i in range(1, len(num_ci)):
    sum_num_ci.append(sum_num_ci[-1] + num_ci[i])

if ((sum(num_ci) > 2*num_LR[1]) or (sum(num_ci) < 2*num_LR[0])):
    print("0")
else:
    for i in range(len(sum_num_ci)):
        if (sum_num_ci[i] >= num_LR[0]) and (sum_num_ci[i] <= num_LR[1]):
            if ((sum_num_ci[-1] - sum_num_ci[i]) >= num_LR[0]) and (sum_num_ci[-1] -sum_num_ci[i] <= num_LR[1]):
                final_result = i + 2
                break
            else:
                final_result = 0
        else:
            final_result = 0
    print(final_result)
