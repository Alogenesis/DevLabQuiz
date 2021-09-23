'''
In : ตัวเลขไม่จำกัดบรรทัด โดยให้ทำการรับตัวเลขไปเรื่อยๆจนกว่าผู้ใช้งานจะใส่ 0 จึงหยุดการรับข้อมูล
บรรทัดต่อไปเป็นประเภทของการเรียงจากหน้ามาน้อย(max) หรือจากน้อยไปมาก(min)

Out : ข้อมูลที่ถูกเรียงลำดับตามคำสั่งแล้วจำนวนหลายบรรทัด
ข้อความบรรทัดสุดท้ายที่เป็น max และ min จะเป็น non-case sensitive

In : 12
32
56
1
4
7
8
3
10
0
MaX

Out : 56 32 12 10 8 7 4 3 1
'''

l = []
a = int(input())
while a != 0 :
    l.append(a)
    a = int(input())
c = input()
c1 = c.lower()
if c1 == 'max' :
    l.sort(reverse = True)
if c1 == 'min' :
    l.sort(reverse = False)
print(' '.join(str(i) for i in l))

