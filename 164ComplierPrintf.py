'''
ตรวจสอบเงื่อนไขว่า ผู้ใช้พิมพ์คำสั่ง printf ถูกต้องหรือไม่
'''

x = input()

correct = 0
incorrect = 0


if 'printf("' in x  and '");' in x:
    correct += 1
    print('Go correct +1')
    spl = x.split('"')
    print(spl[1])

elif 'printf(\\"' in x  and '\\");' in x:
    correct += 1
    print('Go correct +1')
    spl = x.split('"')
    g = spl[1]
    gn = g[0:-1]
    print(gn)
else:
    incorrect += 1
    print('Compile Error!')



