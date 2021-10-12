'''
เราจะสมมติว่าคีย์บอร์ดเรากำลังเล่นเกมอยู่ โดยที่
w = ขึ้น
a = ซ้าย
s = ล่าง
d = ขวา
แล้วเราแสดงผลออกมาว่า เราไปทางไหน
โจทย์จะให้ 4 ชุดปุ่ม ต่อ 1 test

w
w
s
d
^
^
v
>
'''

a = input()
b = input()
c = input()
d = input()

for x in [a,b,c,d]:
    if x == 'w':
        print('^')
    elif x == 'a':
        print('<')
    elif x == 's':
        print('v')
    else:
        print('>')

