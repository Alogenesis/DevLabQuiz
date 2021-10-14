'''
ถ้า
A=1 B=2 C=3 ไปจน Z=26
แปลงจากตัวหนังสือไปเป็นชุดตัวเลข เช่น
iloveyou >> 91215225251521

'''

x = input().upper()

for i in x:
    print((ord(i) - 64), end='')