'''
หาด้านตรงข้ามมุมฉาก ทศนิยม 2 ตำแหน่ง (ถ้ามี)
'''

import math
a = int(input())
b = int(input())

cpow2 = a**2 + b**2
c = math.sqrt(cpow2)

if c - int(c) == 0 :
    print(int(c))
else:
    print(round(c,2))

