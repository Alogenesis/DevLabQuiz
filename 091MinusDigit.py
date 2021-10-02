'''
รับจำนวนเต็มบวกทีละบรรทัดอย่างน้อย 1 จำนวนและบรรทัดสุดท้ายรับจำนวนเต็มลบ
ตัวเลขชุดใหม่ที่เกิดจากการเอาตัวเลขเดิมรวมกับตัวเลขติดลบตัวสุดท้ายนั้น
In :
1
2
3
4
-5
Out :
-4
-3
-2
-1
'''


x_lib = []
y_lib = []
while True:
    user_input = int(input())
    if user_input >= 0 :
        x_lib.append(user_input)
    else:
        y_lib.append(user_input)
        break


#print(x_lib)
#print(y_lib)

for i in x_lib:
    print(i + y_lib[0])