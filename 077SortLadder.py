'''
เรียงเลขตาม input ที่ได้มา
In :
Number: 6 (input + แถวที่ต้องแสดง)
5
13
2
46
22
8

Out :
ROW 1 : [5]
ROW 2 : [5, 13]
ROW 3 : [2, 5, 13]
ROW 4 : [2, 5, 13, 46]
ROW 5 : [2, 5, 13, 22, 46]
ROW 6 : [2, 5, 8, 13, 22, 46]
'''

nx = input()
x = int(nx[-1])
print(x)
num_lib = []
for i in range(0,x):
    a = int(input())
    num_lib.append(a)
    num_lib.sort()
    print('ROW', (i+1),':',num_lib)
