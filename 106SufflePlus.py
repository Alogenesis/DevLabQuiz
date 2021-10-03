'''
ให้สลับเลขระหว่าง หลักสิบ กับ หลักหน่วย แล้วนำมาบวกกัน
เช่น
36 + 25 = 63 + 52 (สลับในตัวมันเอง)

In :
78
+
36

Out : 87 + 63 = 150
'''
x = input()
y = input()
z = input()
xa = x[1]
xb = x[0]
#print(xa,xb,sep='')
xn = '{}{}'.format(xa,xb)#xa,xb,sep=''
xint = int(xn)
print(xint)

za = z[1]
zb = z[0]
zn = '{}{}'.format(za,zb)
zint = int(zn)
print(zint)

print(xint,y,zint,'=',(xint+zint))