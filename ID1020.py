#!/usr/bin/python3 
def multi( *num ):
    result = 1
    for i in range(len(num)):
        if (isinstance(num[i],(int,float))):
            # 判断数据是否是实数
            result = num[i]*result
        else:
            result = "Invalid arg " + str(i + 1)
            break
    return result

print(eval(input()))
