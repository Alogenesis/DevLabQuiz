'''
เขียนโปรแกรมเพื่อนับจำนวนอักษรระหว่างพิมพ์เล็กกับพิมพ์ใหญ่ของ String ว่ามีอย่างละกี่ตัว

Hello world!
UPPER:1
LOWER:9
'''

x = input()
lower = 0
upper = 0

for i in x:
    if i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    else:
        pass

print('UPPER:',upper,sep='')
print('LOWER:',lower,sep='')