#!/usr/bin/python3 
scale = int(input())

print('------start------')
for i in range(scale+1):
    a = '**' * i
    b = '..' * (scale-i)
    c = (i/scale)*100
    print('{:3.0f} %[{}->{}]'.format(c,a,b))
print('------end-----')