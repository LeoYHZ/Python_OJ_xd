#!/usr/bin/python3 
score = list(map(int, input().split(" ")))
result = 0.2*score[0] + 0.3*score[1] + 0.5*score[2]
print(int(result))
