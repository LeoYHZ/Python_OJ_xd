#!/usr/bin/python3

def f(x): 
    for i in range(3,x+1):
        global cnt
        y = cnt[-1]
        z = 0
        for j in range(2, i): 
            y += 1
            if i % j == 0: 
                cnt.append(y)
                z = 1
                break
        if z == 0:
            cnt.append(y) 
                
line = []
cnt = [0,0,0]
try :
    while (1):
        line.append(eval(input()))
except EOFError:
    pass
f(max(line))
for i in line:
    print(cnt[i])