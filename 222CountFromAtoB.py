'''
นับตั้งแต่ a ถึง b
'''

x = int(input())
y = int(input())
for i in range(x,y+1):
    print(i,end=' ')

if x == 0 and y < x:
    for i in range(x, y-1 , -1):
        print(i, end=' ')