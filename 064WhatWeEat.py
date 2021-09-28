'''
ครอบครัวหนึ่งมีสมาชิกอยู่ 4 คน ได้แก่ พ่อ แม่ พี่ชาย และน้องสาว
มีอาหารอยู่ 2 อย่างคือ ข้าวมันไก่ และก๋วยเตี๋ยว
ครอบครัวนี้ได้ทำการโหวตว่าจะเลือกกินอย่างไหน
โดยที่อาหารชนิดไหนได้รับการโหวตมากสุดจะได้รับเลือกเป็นเมนูที่ครอบครัวจะกิน
แต่ถ้าผลโหวตเท่ากันให้เมนูที่น้องสาวเลือกเป็นเมนูที่ครอบครัวนี้จะกิน
# ข้าวมันไก่ = Chicken rice, ก๋วยเตี๋ยว = Noodle

In :                    Out :
Chicken rice                Chicken rice
Noodle
noodle
chicken rice (น้อง)
'''

chick = 0
noodle = 0
noodle_sp = 0
chick_sp = 0
for i in range(0,3):
    x = input('>> ').lower()
    if x == 'chicken rice':
        chick += 1
    elif x == 'noodle':
        noodle += 1
    print('i =',i)
    print('----------------------')

y = input('>> ').lower()
if y == 'noodle':
    noodle_sp += 1
    noodle += 1
else:
    chick_sp += 1
    chick += 1
print('----------------------')
if chick > noodle:
    print('Chicken rice')
elif noodle > chick:
    print('Noodle')
elif chick == noodle and noodle_sp == 1:
    print('Noodle')
elif chick == noodle and chick_sp == 1:
    print('Chicken rice')
else:
    pass
