#!/usr/bin/python3 
stopword = ''
stri = ''
try:
    for line in iter(input, stopword):
        stri += line + '\n'
except EOFError:
   pass
stri = stri[0:-1]

count_space = 0
count_numbers = 0
count_letters = 0
count_other = 0
for i in stri:
    if (i == " "):
        count_space += 1
    elif (i >= "0") and (i <= "9"):
        count_numbers += 1
    elif (i >= "A") and (i <= "z"):
        count_letters += 1
    else:
        count_other += 1

print("%d spaces, %d numbers, %d letters, %d other characters." %(count_space, count_numbers, count_letters, count_other))