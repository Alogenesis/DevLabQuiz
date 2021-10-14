'''
หาว่าจำนวนที่ได้รับเป็นจำนวนบวก จำนวนติดลบ หรือเป็น 0
'''

x = float(input())

if x == 0:
    print('00 Zero 00')
elif x > 0:
    print('++ Positive ++')
else:
    print('-- Negative --')