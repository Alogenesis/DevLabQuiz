'''
In :
3 // บรรทัดแรกสุดบอกจำนวนลูกค้า
K P //ลูกค้าคนที่ 1
1990
Male
A A //ลูกค้าคนที่ 2
2010
Male
Sommai KraiMakMak //ลูกค้าคนที่ 3
1950
Male

out : --Customers Information--
K P (age : 27)
A A (age : 7)
Sommai KraiMakMak (age : 67)
'''

get = int(input())
print('--Customers Information--')
for i in range(get):
    name = input()
    byear = int(input())
    age = 2017 - byear
    sex = input()
    print(name, '(age : {})'.format(age))
