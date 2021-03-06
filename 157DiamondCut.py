'''
ช่างเจียระไนได้รับเพชร 2 มิติ ทรงสี่เหลี่ยมจัตุรัสด้านละ n หน่วย ต้องการตัดมุมแต่ละมุมด้านเท่า ๆ กันด้านละ r หน่วย
ซึ่ง r ต้องน้อยกว่าครึ่งของ n ยิ่งตัดลึก มุมยิ่งออกมาเป็นรูปสามเหลี่ยมมุมฉาก
ดังนั้น ช่างจึงขอให้คุณช่วยเขียนโปรแกรมแสดงผลเป็นรูปของเพชรที่เจียระไนตัดมุมเรียบร้อยแล้ว
กำหนดให้ "*" แทนเพชรขนาด 1 หน่วย และ "-" แทนช่องว่าง ดังตัวอย่าง
ตัวอย่างที่ 1 เมื่อ n=8,r=0
********
********
********
********
********
********
********
******** สังเกตว่าจะไม่มีการตัดมุม ดังนั้นไม่มีช่องว่าง
ตัวอย่างที่ 2 เมื่อ n=8,r=1
-******-
********
********
********
********
********
********
-******- มีการตัดมุม 1 หน่วย
ตัวอย่างที่ 3 เมื่อ n=8,r=3
---**---
--****--
-******-
********
********
-******-
--****--
---**--- มีการตัดมุม 3 หน่วย ช่องว่างเป็นรูปสามเหลี่ยมมุมฉาก
'''

x = input()
xx = x.split(' ')
n = int(xx[0])
r = int(xx[1])

half = int(n/2)

# Uncut Diamond
uncut = []
for i in range(0,half):
    uncut.append('*'*n)
print(uncut)

# cut Diamond
cutter = []
for i in range(0,r):
    x = '-'*(i+1) + '*'*(n-(2 + i*2)) + '-'*(i+1)
    cutter.append(x)
cutter.reverse()
print(cutter)


# Replace cut diamond to uncut
for i in range(0,len(cutter)) :
    uncut[i] = cutter[i]
print(uncut)

for i in uncut:
    print(i)
for i in reversed(uncut):
    print(i)