'''
นายป.และผองเพื่อนได้นั่งเล่นเกมนับเลขแบบชิวๆ
โดยเลขที่นับนั้นจะเริ่มนับเลขแรกด้วยเลข 1 และตัวต่อไปจะเป็นจำนวนที่มีตัวประกอบ 3 11 19 (เลขที่นับจะประกอบด้วย 3 หรือ 11 หรือ 19 เท่านั้น)
ตามลำดับจากน้อยไปมากไปเรื่อยๆ
แต่เนื่องจากนายป. นั้นเป็นคนที่นับเลขค่อนข้างจะช้าจึงขอให้คุณที่เป็นโปรแกรมเมอร์สุดโหดช่วยหาลำดับ n ของเลขที่ต้องนับ
ตัวอย่างเช่น
n = 10
จำนวนตามลำดับคือ
1 (1)
3 (3)
9 (3*3)     9   *3(0)
11 (11)     11  *3(0)
19 (19)     19  *3(0)
27 (3*3*3)  9   *3(1)
33 (3*11)   11  *3(1)
57 (3*19)   19  *3(1)
81 (3*3*3*3) 9  *3*3(2)
99 (3*3*11)  11 *3*3(2)
ดังนั้นจำนวนตัวที่ 10 คือ 99

'''


def maxDivide(a, b):
    while a % b == 0:
        a = a / b
    return a


# ฟังก์ชั่นที่เช็คว่าเป็นตัวประกอบจริงมัย
def isUgly(no):
    no = maxDivide(no, 3)
    no = maxDivide(no, 11)
    no = maxDivide(no, 19)
    return 1 if no == 1 else 0


# ฟังก์ชั่นรับตัวที่ n
def getNthUglyNo(n):
    i = 1

    # นับตัวประกอบ
    count = 1

    # เชคเลขทุกตัวจนเจอตัวประกอบ
    # นับตัวประกอบให้เป็น n
    while n > count:
        i += 1
        if isUgly(i):
            count += 1
    return i


# รันโค๊ด
no = getNthUglyNo(int(input()))
print(no)


