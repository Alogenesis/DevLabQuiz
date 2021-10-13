'''
ช่วงนี้ร้านแพนเค้กขาดทุน ดังนั้นจึงจัดโปรโมชั่นใหม่ ดังนี้
แถมคูปองและถาดรองแพนเค้กให้ โดย 1 คูปอง/ชิ้น และ 1 ถาด/ชิ้น ทุกครั้งที่ได้รับแพนเค้กจากร้านนี้
เมื่อสะสมครบ 2 คูปอง จะสามารถนำมาแลกแพนเค้กเพิ่มได้ 1 ชิ้นฟรี
เมื่อสะสมครบ 4 ถาด จะสามารถนำมาแลกแพนเต้กเพิ่มได้ 1 ชิ้นฟรี
คุณเป็นโปรแกรมเมอร์หัวไว เมื่อเห็นโปรโมชั่นของร้านนี้แล้ว
จึงกลับมาคิดว่า ถ้ามีเงินอยู่ n บาท
และแพนเค้กชิ้นละ k บาท
จะได้รับแพนเค้กมากสุดกี่ชิ้น???

In : มีบรรทัดเดียว รับจำนวนเต็ม 2 จำนวน n,k คั่นด้วยช่องว่าง 1 ช่อง แทนเงินของคุณและราคาแพนเค้กต่อชิ้นตามลำดับ
>> 20 3  (20 มีตัง 3 ชิ้นละ)
Out : มีบรรทัดเดียว แสดงผลเป็นจำนวนแพนเค้กมากสุดที่จะได้รับ
>> 19 (ได้ทั้งหมดชิ้น)
'''

str_input = input()
cash_str,cost_str = str_input.split(' ')
cash = int(cash_str)
cost = int(cost_str)
remain = cash

coupon = 0
base = 0
pancake = 0

print('Remain coupon base =', remain , coupon , base, pancake)
while True:
    if remain >= cost:
        remain = remain - cost
        coupon += 1
        base += 1
        pancake += 1
    elif coupon >= 2:
        coupon -= 2
        pancake += 1
        coupon += 1
        base += 1
    elif base >= 4:
        base -= 4
        pancake += 1
        coupon += 1
        base += 1
    else: #เงินไม่พอ ของแลกไม่พอ
        break
    print('Remain coupon base =', remain, coupon, base, pancake)

#Answer Output
print(pancake)



