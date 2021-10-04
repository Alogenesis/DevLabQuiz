'''
นาย A ต้องการส่งจดหมายรักให้กับนางสาว B ซึ่งทั้งคู่จะมีสูตรในการคำนวนการเข้ารหัสที่ทั้งสองเข้าใจด้วยกันอยู่
เช่น ~ss = zoo
In : บรรทัดที่ 1 รับข้อความจากผู้ใช้
I Love You
You're mine
EternalLove...<3
Out : แสดงผลข้อความที่ถูกเข้ารหัส
M$Pszi$]sy
]sy+vi$qmri
IxivrepPszi222@7
'''

x = 'I Love You'


for i in x:
    print(chr(ord(i) + 4) , end='')