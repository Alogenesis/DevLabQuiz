'''
รับจำนวนจริงบวกเข้ามาเรื่อยๆ หยุดเมื่อจำนวนนั้นไม่ใช่จำนวนจริงบวก และหาค่าเฉลี่ยของจำนวนที่รับมา
In :
1
2
3
-1
Out : 2.0
'''

x = 0
y = []
while x >= 0:
    x = int(input())
    if x >= 0:
        y.append(x)
print(y)

sum_val = 0
for i in y:
    sum_val = sum_val + i
print(sum_val)
print(sum_val/(len(y)))