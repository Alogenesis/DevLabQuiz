'''
สู้กับมอนเตอร์เพื่อจะได้Exp และไปอัพLv กันเถอะ
โดยมีแนวทางดังนี้อย่างแรกต้องแยกเอาตัวเลขออกมาเพื่อทำการคำนวณต่อไปเช่น Received 100 EXP from battle ก็ให้นำเอาเลข100ออกมาเพื่อ นำไปคิดต่อโดยที่มีสูตรการคิดของแต่ละเลเวลอยู่ว่า
maxexp = lv*100
ATK = lv*10
HP = lv*100
รูปเเบบ Input
รับExp ที่ได้จากการสู้กับมอนเอตร์
รูปเเบบ Output
แสดงเลเวลปัจจุบัน พร้อมทั้งความสามารถของตัวละครในเลเวลนั้นๆ

In : Received 0 EXP from battle
Lv : 1
Exp : 0/100
ATK : 10
HP : 100

Received 350 EXP from battle
Lv : 3          (Lv.1 = 100  / Lv.2 = 200  / Lv.3 = 300 )
Exp : 50/300 (exp เกิน)
ATK : 30 (lv*10)
HP : 300 (lv*100)
'''

import re

lv = 1
atk = lv*10
hp = lv*100
max_exp = lv*100
receive_exp = input()
rec_exp = int(re.search(r'\d+', receive_exp).group())

#print(rec_exp)
#print(type(rec_exp))
exp_left = rec_exp

while max_exp <= exp_left:
    print('start at',exp_left)
    exp_left = exp_left - (max_exp)
    lv = lv +1
    atk = lv * 10
    hp = lv * 100
    max_exp = lv * 100
    print('exp left',exp_left)
    print('status')
    print('Lv.',lv , 'hp',hp ,'atk', atk)
    print('--------------------------------')

print('Lv :',lv)
print('Exp :',str(exp_left)+'/'+str(max_exp))
print('ATK :',atk)
print('HP :',hp)
