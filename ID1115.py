#!/usr/bin/python3
import json

num_N = int(input())
data_list = []
for i in range(num_N):
    data_list.append(json.loads(input()))

def h_index(list):
    global index
    num = 0
    for i in list:
        if (i >= index):
            num += 1
    if (num > index):
        index += 1
        h_index(list)
    elif (num < index):
        index -= 1
    else:
        pass

result_dict = {}
for i in range(num_N):
    for j in (data_list[i]["authors"]["authors"]):
        try:
            result_dict[j["full_name"]].append(data_list[i]["citing_paper_count"])
        except KeyError:
            result_dict[j["full_name"]] = [data_list[i]["citing_paper_count"]]

output_dict = {}
list_name = result_dict.keys()
for i in list_name:
    index = 0
    h_index(result_dict[i])
    output_dict[i] = index

output_list = sorted(output_dict.items(), key = lambda kv:(-kv[1], kv[0]))

for i in output_list:
    print("{} {}".format(i[0], i[1]))