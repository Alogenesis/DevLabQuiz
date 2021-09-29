'''
สลับ Upper Lower
'''

x = input()
y = []
for i in x:
    if i.islower():
        y.append(i.upper())
    elif i.isupper():
        y.append(i.lower())
    elif i.isdigit():
        y.append(i)
    else:
        y.append(i)
for j in y:
    print(j,end='')
