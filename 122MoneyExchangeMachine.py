'''
โปรแกรมจะรับค่าจำนวนเงินที่ต้องการแลกมาและคำนวนออกมาว่าจะได้ ธนบัตรและเหรียญใดบ้าง
จำนวนธนาบัตร ประเภทใดบ้างได้จำนวนกี่ฉบับ และจำนวนเหรียญชิดใดบ้าง ชนิดละกี่เหรียญ และแสดงผลรวมเงินที่ต้องการแลกทั้งหมด
เครื่องนี้เป็นเครื่องรุ่นเก่ายังไม่สามารถแลกเหรียญสตางค์ได้
ธนาบัตร มี 5 ชนิด
1.ชนิดฉบับละ 1,000 บาท
2.ชนิดฉบับละ 500 บาท
3.ชนิดฉบับละ 100 บาท
4.ชนิดฉบับละ 50 บาท
5.ชนิดฉบับละ 20 บาท
เหรียญ มี 3 ชนิด
1.ชนิดเหรียญละ10 บาท
2.ชนิดเหรียญละ 5 บาท
3.ชนิดเหรียญละ 1 บาท
'''

x = int(input())
xn = x
thousand = 0
fivehundred = 0
onehundred = 0
fifty = 0
twenty = 0
ten_coin = 0
five_coin = 0
one_coin = 0

while x != 0:
    if x >= 1000:
        x -= 1000
        thousand += 1
    elif x >= 500:
        x -= 500
        fivehundred += 1
    elif x >= 100:
        x -= 100
        onehundred += 1
    elif x >= 50:
        x -=50
        fifty += 1
    elif x >= 20:
        x -= 20
        twenty += 1
    elif x >= 10:
        x -= 10
        ten_coin += 1
    elif x >= 5:
        x -= 5
        five_coin += 1
    elif x >= 1:
        x -= 1
        one_coin += 1

if thousand > 0:
    print('ธนบัตร 1,000฿ :', thousand,'ฉบับ')
if fivehundred > 0:
    print('ธนบัตร 500฿ :', fivehundred,'ฉบับ')
if onehundred > 0:
    print('ธนบัตร 100฿ :', onehundred,'ฉบับ')
if fifty > 0:
    print('ธนบัตร 50฿ :', fifty,'ฉบับ')
if twenty > 0:
    print('ธนบัตร 20฿ :', twenty,'ฉบับ')
if ten_coin > 0:
    print('เหรียญ 10฿ :', ten_coin,'เหรียญ')
if five_coin > 0:
    print('เหรียญ 5฿ :', five_coin,'เหรียญ')
if one_coin > 0:
    print('เหรียญ 1฿ :', one_coin,'เหรียญ')

print('จำนวนเงินที่แลกทั้งหมด {:,} บาท'.format(xn))
