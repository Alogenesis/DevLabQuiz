'''
In :
2 + 2
3 * 5
4 - 6

Out :
2 + 2 = 4
2 + 2 = 4
4 - 6 = -2
'''

x1,o,y1 = input().split(' ')
x = int(x1)
y = int(y1)

if o == '+':
    print(x,'+',y,'=',x+y)
elif o == '-':
    print(x, '-', y, '=', x - y)
elif o == '*':
    print(x, '*', y, '=', x * y)
elif o == '/':
    print(x, '/', y, '=', x / y)