'''
จงเขียนโปรแกรมรับค่าจากผู้ใช้ 5 ตัว หากมีตัวเลข"อย่างน้อย" 3 ตัว
ตรงกับตัวเลขหวยในฝันของน้องจอย ให้แสดงผลลัพธ์ว่า You are lucky แต่ถ้าไม่ ให้แสดงว่า You are unlucky

ฝัน : 8, 14, 112, 76, 2
'''

lucky_num = [8,14,112,76,2]
dream_num = []
correct = 0
for i in range(0,5):
    x = int(input())
    dream_num.append(x)

for j in lucky_num:
    for k in dream_num:
        if k == j:
            correct += 1
        else:
            pass

if correct >= 3 :
    print('You are lucky')
else:
    print('You are unlucky')


