'''
สร้างบันได ขั้นตาม input
5
=
==
===
====
=====
'''

x = int(input())
n = 1
for i in range(0,x):
    for j in range(0,n):
        print('=',end='')
    print()
    n += 1