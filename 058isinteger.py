'''
หาว่า รากที่สองของจำนวนที่รับมาเป็น int มั้ย
'''
import math

x = int(input())
a = math.sqrt(x)
#print(a)


if a.is_integer() == True :
    print('Integer')
else:
    print('Float')