'''
หา sqrt เลขที่ลงท้ายด้วย 25 ถ้าไม่มีเลขที่ลงด้วย int คืนค่า No Numbers Matching!

In :
25 / 5
2025 / 45
31625 / No Numbers Matching!
'''

import math

x = int(input())
y = math.sqrt(x)

if y.is_integer():
    print(int(y))
else:
    print('No Numbers Matching!')