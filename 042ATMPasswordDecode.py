'''
รับรหัสมา แกะออก
รับมา HE45L32LO458T6H359ISIS1BO589RNT34ODEVN80AJA
เอาเฉพาะตัวเลขมาบวกกัน
45+32+458+6+359+1+589+34+80 = 1604
โดยถ้าหากผลรวมที่ได้น้อยกว่า 4 หลักให้ทำการเติมเลข 0 ไปด้านหน้า
เช่น
a1b2c3d4e5f6g7h8i9
0045
'''



x = input('>> ')
digit = []
for i in x:
    if i.islower():
        print('lower')
        digit.append('.')
    elif i.isupper():
        print('upper')
        digit.append('.')
    elif i == '-':
        digit.append('.')
    elif i == '*':
        digit.append('.')
    elif i == '!':
        digit.append('.')
    elif i == '@':
        digit.append('.')
    elif i == '#':
        digit.append('.')
    else:
        print('Digit')
        digit.append(i)

print(digit)
string_digit = (''.join(str(x) for x in digit))
print(string_digit)  #txt
print(type(string_digit))
sep_lib = string_digit.split('.')
print(sep_lib)
print(len(sep_lib))

digit_code = []
for a in sep_lib:
    if a.isdigit():
        digit_code.append(a)
    else:
        pass
print(digit_code)

sum = 0
for b in digit_code:
    sum = sum + int(b)
print(sum)

member = len(str(sum))
if member == 2:
    print('00',end='')
    print(sum)
elif member == 3:
    print('0', end='')
    print(sum)
else :
    print(sum)

