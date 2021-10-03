'''
รับ input มาสองจำนวน แล้วหาผลบวก แล้วคูณตัวมันเอง
'''

x = input()
y = input()
z = 0
try:
    x = int(x)
    y = int(y)
except:
    print('Error')
    z += 1
'''
try:
    
except:
    print('Error')
    z += 1
'''
if z == 0:
    n = x+y
    print('{:,}'.format(n * n))
else:
    pass