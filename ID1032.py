#!/usr/bin/python3
import re

def judge_passwd( passwd_str ):
    if ((len(passwd_str) >= 8) and (len(passwd_str) <= 16)):
        # print("YES")
        judge_flag = 0
        if (re.findall(r'[A-Z]', passwd_str)):
            judge_flag += 1
        if (re.findall(r'[a-z]', passwd_str)):
            judge_flag += 1
        if (re.findall(r'\d', passwd_str)):
            judge_flag += 1
        if (re.findall(r'[\~\!\@\#\$\%\^]', passwd_str)):
            judge_flag += 1
        if (judge_flag >= 3):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

    
# 参考文章https://blog.csdn.net/weixin_38819889/article/details/102630312
# https://blog.csdn.net/u012421852/article/details/79300356

passwd = []

for i in range(int(input())):
    passwd.append(input())

for i in range(len(passwd)):
    judge_passwd(passwd[i])