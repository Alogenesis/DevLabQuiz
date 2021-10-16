'''
ณ ฟาร์มแห่งหนึ่ง มีเจ้าของฟาร์มที่ไม่ค่อยจะปกติสักเท่าใหร่ เค้าไม่อยากรู้จำนวนสัตว์เลี้ยงในฟาร์มของเขา แต่เขากลับอยากรู้จำนวนขาของสัตว์ในฟาร์มมากกว่า
ให้ทุกคนเขียนโปรแกรมหาจำนวนขาของสัตว์ในฟาร์ม
โดยที่ในฟาร์มมีสัตว์ดังนี้ สุนัข แมว ไก่ เป็ด วัว งู นก
ข้อมูลเพิ่มเติม เผื่อใครไม่รู้
สุนัขมี 4 ขา
แมวมี 4 ขา
ไก่มี 2 ขา
เป็ดมี 2 ขา
วัวมี 4 ขา
งู ไม่มีขา
นกมี 2 ขา

ให้ชื่อและจำนวนสัตว์แต่ละชนิด จำนวน 3 ชนิด
เช่น
Cow 3
Dog 2
Bird 4

Output เป็นจำนวนขาทั้งหมด
เช่น
28
'''

dog = 4
cat = 4
cow = 4

chicken = 2
duck = 2
bird = 2

snake = 0

a1 = input()
a2 = input()
a3 = input()

a1sp = a1.split(' ')
a1t = a1sp[0]
a1m = int(a1sp[1])

a2sp = a2.split(' ')
a2t = a2sp[0]
a2m = int(a2sp[1])

a3sp = a3.split(' ')
a3t = a3sp[0]
a3m = int(a3sp[1])

def animal_leg(type,multi):
    leg = 0
    if type == 'Dog' or type == 'Cat' or type == 'Cow' :
        leg += 4
    elif type == 'Chicken' or type == 'Duck' or type == 'Bird' :
        leg += 2
    else:
        leg += 0

    multiplyer = multi

    return leg * multiplyer

a1leg = animal_leg(a1t,a1m)
a2leg = animal_leg(a2t,a2m)
a3leg = animal_leg(a3t,a3m)

print(a1leg + a2leg + a3leg)