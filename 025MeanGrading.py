'''เกรดเฉลี่ย
In : 3.5
2.0
4.0
2.0
2.5

Out :
THAI = 3.5
MATH = 2.0
ENGLISH = 4.0
SCIENCE = 2.0
SPORT = 2.5
---
GPA = 2.8
'''

a = float(input('Type a number : '))
b = float(input('Type a number : '))
c = float(input('Type a number : '))
d = float(input('Type a number : '))
e = float(input('Type a number : '))

print('THAI =',a)
print('MATH =',b)
print('ENGLISH =',c)
print('SCIENCE =',d)
print('SPORT =',e)
print('---')
print('GPA =', (a+b+c+d+e)/5 )