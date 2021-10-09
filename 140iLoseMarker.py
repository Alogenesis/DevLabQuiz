'''
ไอซ์ได้ทำปากกาหายทั้งหมด n ด้ามโดยแต่ละแท่งราคาไม่เท่ากัน ซึ่งในการไป
ซื้อไอซ์ได้ฝากภูเขาไปซื้อที่ร้านซึ่งภูเขาก็คิดค่าปากกาเพิ่มขึ้น แท่งละ x เปอร์เซ็นต์
ถ้าเปอร์เซ็นต์ที่คิดแล้วติดทศนิยมจะปัดขึ้นเป็นจำนวนเต็มทั้งหมด งานของคุณคือหาว่าไอซ์ต้องจ่ายเงินภูเขากี่บาท
(การคิดราคาเพิ่มจะคิดจากราคาละแท่ง ไม่ได้คิดเพิ่มยอดรวม)


In :
2 50 (n = 2 ด้าม / x = 50% คิดเพิ่ม)
1 2 (ราคาปากกาแต่ละด้าม)

Out : 5
'''
from decimal import Decimal
import math
z = '15 56' #input()
xr,nr = z.split(' ')
lose = int(xr)
plus = int(nr)
print(lose,plus)
y = '4 5 6 8 9 5 6 9 4 20 77 8 9 99 100' #input()

cost_lib_str = y.split(' ')
cost_lib = []
for i in cost_lib_str:
    cost_lib.append(int(i))
print(cost_lib)

new_cost = []
serve = []
n = 0
percent = plus/100
extra = Decimal(str(percent))
print(extra)
for i in cost_lib:
    n = math.ceil(i * extra) + i
    o = (i * extra) + i
    new_cost.append(n)
    serve.append(o)
    n = 0
    o = 0
print(new_cost)
print(serve)

sum = 0

for i in new_cost:
    sum = sum + i

print(sum)
