'''
ให้หาว่าใครตั้ง Password ที่ยากที่จะถูก hack จากผู้ไม่ประสงค์ดีมากที่สุด ระหว่าง Man, Non และ Miv ตามลำดับ โดยมีเกณฑ์ในการตั้ง Password ที่ดีดังนี้
ตัวอักษร a-z อย่างน้อย 1 ตัว
ตัวเลข 0-9 อย่างน้อย 1 ตัว
ตัวอักษร A-Z อย่างน้อย 1 ตัว
ตัวอักษรพิเศษ $ หรือ # หรือ @ อย่างน้อย 1 ตัว
ความยาวไม่น้อยกว่า 6 ตัว และ ไม่มากกว่า 12 ตัว


ลำดับของคน Man, Non และ Miv
In : ABd1234@1,a F1#2w3E*,2We3345
Out : ABd1234@1 (Man)
'''

user_input = '82Ue#,1 2ewW22,#$Mp445'
spl = user_input.split(',')
print(spl)

upper = 0
lower = 0
number = 0
special = 0

secure_lib = []
secure_level = 0

# run spl member
for i in spl:
    print(i)
    # run string in single member
    for j in i:
        print(j)
        if j.isupper():
            upper += 1
        elif j.islower():
            lower += 1
        elif j.isnumeric():
            number += 1
        elif j == ' ':
            pass
        else:
            special += 1
        print('ULNS =',upper,lower,number,special)

    for k in [upper,lower,number,special]:
        print('ULNS for sc lv =',k)
        if k > 0 :
            print('Go upper =',upper)
            secure_level += 1
            print('secure Lv =', secure_level)
        elif k > 0 :
            print('Go lower =', lower)
            secure_level += 1
            print('secure Lv =', secure_level)
        elif k > 0 :
            print('Go number =', number)
            secure_level += 1
            print('secure Lv =', secure_level)
        elif k > 0 :
            print('Go special =', special)
            print('secure Lv before +1',secure_level)
            secure_level += 1
            print('secure Lv =', secure_level)

    if len(i) < 6 or len(i) > 12:
        secure_level = 0
        secure_lib.append(secure_level)
        upper = 0
        lower = 0
        number = 0
        special = 0
        continue
    else:
        secure_lib.append(secure_level)
        print('Now sc lib =',secure_lib)
    secure_level = 0
    print('Now sc lv =', secure_level)
    upper = 0
    lower = 0
    number = 0
    special = 0


print(secure_lib)

man = secure_lib[0]
non = secure_lib[1]
miv = secure_lib[2]

if man >= non and man >= miv:
    print(spl[0],'(Man)')
elif non >= man and non >= miv:
    print(spl[1], '(Non)')
else:
    print(spl[2],'(Miv)')