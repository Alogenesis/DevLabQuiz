'''
นับจาก a ไป b ทีละ c
'''

a = int(input())
b = int(input())
c = int(input())

for i in range(a,b+1,c):
    print(i,end=' ')

'''
if b < a :
    for i in range(b, a + 1, c):
        print(i, end=' ')
'''

if a > b and b < 0:
    print('Go')
    for i in range(a, b-1 , -c):
        print(i, end=' ')