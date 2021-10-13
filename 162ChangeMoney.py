'''
โปรแกรมการทอนเงินให้กับลูกค้า เพื่อแก้ปัญหาการไม่มีทอนหรือเงินขาดมเงินเกิน
ตามแคชเชียร์ ที่ร้านสะดวกซื้อ โดยการ จำแนก ประเภทของธนบัตรในแคชเชียร์และ
นับจำนวนของธนบัตรประเภทนั้นๆ จากนั้นให้โปรแกรมทำการคำนวนเงินทอนและ เลือกประเภทของธนบัตรที่ต้องทอน
เพื่อป้องกัน การทอนธนบัตรผิดชนิด และ เพื่อให้ง่ายต่อการตรวจสอบว่าในแคชเชียร์ในมีธนบัตรแต่ละประเภทเพียงพอที่จะบริการลูกค้าหรือไม่

In :
line 1: รับค่า int = ราคาสินค้า
line 2: รับค่า int = จำนวนเงินที่ลูกค้าชำระ
line 3 - n: รับค่า ประเภทธนบัตร และ จำนวนธนบัตร ในแคชเชียร์

Out :
แสดง จำนวนเงินทอน
ประเภท และ จำนวน ธนบัตรที่ต้องทอน

In :
500
1000
1000 1
500 0
100 3
50 3
20 6
10 10

Out :
change: 500
cash: 100 amount: 3
cash: 50 amount: 2
cash: 20 amount: 5
'''

price = int(input())
cash_get = int(input())
thou_get = input()
fiveh_get = input()
oneh_get = input()
fif_get = input()
twenty_get = input()
ten_get = input()

# Get bank val function
def count_bank(x):
    a1 = x.split(' ')
    a2 = int(a1[1])
    return a2

#get bank Val from input
thousand = count_bank(thou_get)
#print(thousand)
fiveH = count_bank(fiveh_get)
print(fiveH)
oneH = count_bank(oneh_get)
fifty = count_bank(fif_get)
twenty = count_bank(twenty_get)
ten = count_bank(ten_get)

#set base for counting in loop
current = cash_get - price
print('change:',current) #Answer Line 1
thou_c = 0
fiveH_c = 0
oneH_c = 0
fifty_c = 0
twenty_c = 0
ten_c = 0
print(fiveH_c,'fiveH_c')

while current > 0 :
    if current >= 1000 and thousand > 0 :
        current -= 1000
        thou_c += 1
        thousand -= 1
    elif current >= 500 and fiveH > 0 :
        current -= 500
        fiveH_c += 1
        fiveH -= 1
    elif current >= 100 and oneH > 0 :
        current -= 100
        oneH_c += 1
        oneH -= 1
    elif current >= 50 and fifty > 0:
        current -= 50
        fifty_c += 1
        fifty -= 1
    elif current >= 20 and twenty > 0:
        current -= 20
        twenty_c += 1
        twenty -= 1
    elif current >= 10 and ten > 0:
        current -= 10
        ten_c += 1
        ten -= 1
    else:
        print('Go Else')
    print(current,'current')

print(current,'current') #check current to zero?


if thou_c > 0 :
    print('cash: {} amount: {}'.format(1000,thou_c))
if fiveH_c > 0:
    print('cash: {} amount: {}'.format(500, fiveH_c))
if oneH_c > 0:
    print('cash: {} amount: {}'.format(100, oneH_c))
if fifty_c > 0:
    print('cash: {} amount: {}'.format(50, fifty_c))
if twenty_c > 0:
    print('cash: {} amount: {}'.format(20, twenty_c))
if ten_c > 0:
    print('cash: {} amount: {}'.format(10, ten_c))





