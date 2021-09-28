'''
จงเขียนโปรแกรมเรียงไพ่จากน้อยไปมาก โดยมีเงื่อนไขว่า A < 2 < 3 < 4 < 5 < 6 < 7 < 8 < 9 < J < Q < K
In : 5 2 K J A
Out : A 2 5 J K
'''
x = '5 2 K J A'
xx = x.split(' ')
print(xx)
x_lib = []
for j in xx:
    if j == 'A':
        x_lib.append('1')
    elif j not in x_lib:
        x_lib.append(j)
print('x_lib =',x_lib)
x_lib.sort()
print('x_lib =',x_lib)

ans_lib = []
for i in x_lib:
    if i == '1':
        ans_lib.append('A')
    elif i == '2':
        ans_lib.append('2')
    elif i == '3':
        ans_lib.append('3')
    elif i == '4':
        ans_lib.append('4')
    elif i == '5':
        ans_lib.append('5')
    elif i == '6':
        ans_lib.append('6')
    elif i == '7':
        ans_lib.append('7')
    elif i == '8':
        ans_lib.append('8')
    elif i == '9':
        ans_lib.append('9')
    elif i == 'J':
        ans_lib.append('J')
    elif i == 'Q':
        ans_lib.append('Q')
    elif i == 'K':
        ans_lib.append('K')

print(*ans_lib,sep=' ')