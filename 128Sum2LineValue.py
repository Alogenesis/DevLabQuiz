'''
บรรทัดแรกเป็น string ของจำนวนสิ่งของที่เมธีมี
บรรทัดที่ 2 เป็น string ของจำนวนสิ่งของที่เพื่อนมี
จำนวนของที่จะนำมาบวกเกินกว่า 32548 ชื้นให้แสดงว่า Invalid

In :
5 8 9           8 15 89             59847 9598 4784
7 5 2           8 15 8 9            25489 1298 5987

Out :
12 13 11        Invalid             Invalid (เกิน)
'''

x1 = input()
x2 = input()

xl1 = []
xl2 = []

def rearange(a,b):
    a = a.split(' ')
    for i in a:
        b.append(int(i))


rearange(x1,xl1)
rearange(x2,xl2)

#print(xl1)
#print(xl2)

ans = []
for j in range(0,len(xl1)):
    #print(xl1[j] , xl2[j])
    val = xl1[j] + xl2[j]
    ans.append(val)

invalid_count = 0
valid_count = 0
for k in ans:
    if k <= 32548:
        valid_count += 1
    else:
        invalid_count += 1

if invalid_count != 0:
    print('Invalid')
elif len(xl1) != len(xl2):
    print('Invalid')
else:
    for m in range(0,len(ans)):
        print((xl1[m] + xl2[m]),end=' ')