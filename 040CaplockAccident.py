'''
เกิดความผิดพลาดในการพิมพ์โดยระหว่างพิมพ์ได้ลืมกดปุ่ม Capslock ค้างไว้
แปลงกลับซะ
tHIS IS bORNTOdEV > This is BorntoDev
'''



x = input('>> ')
out = []

for i in x:
    if i.isupper():
        #print(i.lower())
        out.append(i.lower())
    elif i.islower():
        #print(i.upper())
        out.append(i.upper())
    else:
        out.append(' ')

#print(out)
for i in out:
    print(i, end='')
