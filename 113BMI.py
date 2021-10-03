'''
BMI
-น้อยกว่า 18 "Thin"
-ระหว่าง 18 - 22 "Good Health"
-ระหว่าง 23 - 24 "Fat Level 1"
-ระหว่าง 25 - 29 "Fat Level 2"
-มากกว่า 30 "Fat Level 3"
โดยคำนวณจาก น้ำหนัก(kg)/ส่วนสูง(m²)
บรรทัดที่ 1 รับค่า น้ำหนักตัว(kg)
บรรทัดที่ 2 รับค่า ส่วนสูง(cm)

in :
55
164
Out :
20.45
Good Health
'''

w = float(input())
t = float(input())
bmi = w / ((t/100)**2)
bmir = round(bmi,2)

print('{:.2f}'.format(bmi))
if bmir > 30:
    print('Fat Level 3')
elif bmir > 25:
    print('Fat Level 2')
elif bmir > 23:
    print('Fat Level 1')
elif bmir >= 18:
    print('Good Health')
else:
    print('Thin')
