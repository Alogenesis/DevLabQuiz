'''
หาค่าที่น้อยที่สุดและมากที่สุดจาก 5 จำนวนที่กำหนด
'''

lib = []
for i in range(0,5):
    x = int(input())
    lib.append(x)

m = min(lib)
mm = max(lib)
print(m,mm,sep=', ')