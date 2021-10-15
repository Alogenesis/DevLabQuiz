'''
มีเงิน จำนวน 2000 บาท
มีรายจ่าย
บรรทัดที่ 1 : ค่าเช่าบ้าน
บรรทัดที่ 2 : ค่าน้ำ
บรรทัดที่ 3 : ค่าไฟ
บรรทัดที่ 4 : ค่าเน็ต
บรรทัดที่ 5 : ค่าโทรศัพท์

รายการค่าใช้จ่าย พร้อมกับคำนวนว่าจะซื้ออะไรกิน
โดยเลือกของที่แพงที่สุดเท่าที่จะซื้อได้ และทำการแสดงผลตามรูปแบบตัวอย่าง test case

บะหมี่กึ่งสำเร็จรูปเส้นเหนียวนุ่ม (chewy noodles) 10 บาท
บะหมี่กึ่งสำเร็จรูปธรรมดา (instant noodles) 6 บาท
น้ำซุปบะหมี่กึ่งสำเร็จรูป (soup) 2 บาท
น้ำประปาดื่มได้ (drinking water) 0 บาท

1000
50
300
299
300

RENT  : 1000 ฿
WATER : 50 ฿
ELEC  : 300 ฿
NET   : 299 ฿
PHONE : 300 ฿
TOTAL : 1000 + 50 + 300 + 299 + 300
        = 1949 ฿
SELECT: chewy noodles
        = 10 ฿
SAVING: 2000 - 1949 - 10
        = 41 ฿
'''
rent = int(input())
water = int(input())
elec = int(input())
net = int(input())
phone = int(input())
total = rent + water + elec + net + phone
left = 2000 - total
buy = 0

print('RENT  : {} ฿'.format(rent))
print('WATER : {} ฿'.format(water))
print('ELEC  : {} ฿'.format(elec))
print('NET   : {} ฿'.format(net))
print('PHONE : {} ฿'.format(phone))
print('TOTAL : {} + {} + {} + {} + {}'.format(rent,water,elec,net,phone))
print('        = {} ฿'.format(total))

if left >= 10 :
    print('SELECT: chewy noodles')
    print('        = 10 ฿')
    buy = 10
    print('SAVING: {} - {} - {}'.format(2000,total,buy))
    print('        = {} ฿'.format(2000-total-buy))
elif left >= 6 :
    print('SELECT: instant noodles')
    print('        = 6 ฿')
    buy = 6
    print('SAVING: {} - {} - {}'.format(2000, total, buy))
    print('         = {} ฿'.format(2000 - total - buy))
elif left >= 2 :
    print('SELECT: soup')
    print('        = 2 ฿')
    buy = 2
    print('SAVING: {} - {} - {}'.format(2000, total, buy))
    print('         = {} ฿'.format(2000 - total - buy))
else:
    print('SELECT: drinking water')
    print('        = 0 ฿')
    buy = 0
    print('SAVING: {} - {} - {}'.format(2000, total, buy))
    print('         = {} ฿'.format(2000 - total - buy))
