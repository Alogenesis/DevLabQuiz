'''
คำอธิบาย
กำหนดให้ f(n)=f(n-1)+100 เมื่อ n>0 และ f(0)=1

รูปเเบบ Input : 5
ค่าของ n
รูปเเบบ Output : 501
ผลลัพธ์ที่ผ่านการคำนวนใน recursive function (ถ้า n < 0 ให้ return -1)
'''


def f(n):
    if n==0:
        return 1
    elif n < 0:
        return -1
    else:
        return f(n-1)+100

n=int(input())
print(f(n))