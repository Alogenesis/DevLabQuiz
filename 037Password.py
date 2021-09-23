'''
ให้ทำการเขียนโปรแกรมการตั้ง password โดยมีเงื่อนไขว่า
ต้องมีตัวอักษรอย่างน้อย 3 ตัวอักษร
และไม่เกิน 20 ตัวอักษร โดยจะ
ต้องมีอักษรพิมพ์ใหญ่อย่างน้อย 1 ตัวอักษร
ตัวพิมพ์เล็กอย่างน้อย 1 ตัวอักษร
ตัวเลขอย่างน้อย 1 ตัวอักษร
และสัญลักษณ์ อย่างน้อย 1 ตัวอักษร
หาสามารถใช้ได้ให้แสดงค่า Valid และไม่ครบเงื่อนไขให้ใช้ค่า Invalid

In :
P@ssword
O10adkspoa/2
9(a[\\\'1\\\"ZXOG<[]dfgoakm

Out :
Invalid
Valid
Invalid

'''

'''
ถ้า index 0 == digit
int +1
ถ้า index 0 == str

(i.islower())
(i.isupper())
(i.isdigit())
if(i=='@'or i=='$' or i=='_'):
'''
password = input('Password : ')
print(password)
print(type(password))

lower = 0
upper = 0
digit = 0
sp = 0

for i in password:
  #print(i)
  if i.islower():
    lower += 1
    print(lower)
  elif i.isupper():
    upper += 1
    print(upper)
  elif i.isdigit():
    digit += 1
    print(digit)
  else:
    sp += 1
    print(sp)

print('All Char')
print(len(password))
print('Lower =', lower)
print('Upper =', upper)
print('Digit =', digit)
print('SP =', sp)


if lower >= 1 and upper >= 1 and digit >= 1 and sp >= 1 and len(password) >= 3 and len(password) <= 20:
  print('Valid')
else:
  print('Invalid')

