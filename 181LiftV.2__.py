'''
เราจะมีลิฟท์ทั้งหมด 5 ชั้น ได้แก่ 1 2 3 4 และ 5 โดยจะอยู่ที่ชั้น 1 เสมอ
และเราจะรับข้อมูลชั้นที่อยากจะไป(อาจมีหลายชั้น)
แล้วแสดงข้อมูลทีละ step โดย รูปแบบดูได้ที่ out put
ถ้ากรอกตัวเลขชั้นไม่ตรงกับที่มีอยู่ ให้ แสดง ว่า
Error! Not have this floor

รับเลขชั้น(จำนวนเต็ม Integer) แล้วจบด้วยตัว - คือจบ input แล้วเช่น
1
-
ถ้ามีหลายชั้นจะ input เป็น
1 ชั้น 1 บรรทัด เช่น
1
3
4
-
โดยเลขชั้นจะเรียงจากน้อยไปมากหรือมากไปน้อยก็ได้

รูปเเบบ Output รูปแบบคือ

OK! Wait please
---------------
Lift is arriving!
---------------
Lift is going up!
---------------
Lift has reached the (ชั้นตามด้วย *ตัวตามหลังอันดับ*) floor!
---------------
Lift is going up!
---------------
Lift has reached the (ชั้นตามด้วย *ตัวตามหลังอันดับ*) floor!
---------------
...ไปเรื่อยจนหมดทุกชั้นที่รับinputมา...
(-) 15 ตัว
ตัวตามหลังอันดับ เช่น 1st 2nd 3 rd 4th ...
ชั้นที่ output ออกมาทีละชั้นให้เรียงจากน้อยไปมาก โดยขั้นด้วย ประโยค "Lift is going up!"

ถ้ากรอกตัวเลขชั้นไม่ตรงกับที่มีอยู่
หรือ หากมีการตรวจเจอชั้นที่ไม่มีตามในโจทย์แม้แต่ 1 อัน
ให้แสดงว่า
Error! Not have this floor
แล้วจบ
'''

floor_list = []
stop = 0
user_input = input()
if user_input != '-':
    floor_list.append(user_input)

while user_input != '-':
    if int(user_input) <= 0 or int(user_input) >= 6:
        print('Error! Not have this floor')
        stop += 1
        break

    else:
        user_input = input()
        if user_input != '-':
            floor_list.append(user_input)
        else:
            break

floor_list.sort()
#print(floor_list)

#รันต่อหรือไม่ต่อ
if stop > 0 :
    pass
else:
    #ก่อนขึนชั้น
    print('OK! Wait please')
    print('---------------')
    print('Lift is arriving!')
    print('---------------')

    #ขึ้นชั้น
    while len(floor_list) > 0 :
        if floor_list[0] == '1' :
            print('Lift is going up!')
            print('---------------')
            print('Lift has reached the 1st floor!')
            print('---------------')
        elif floor_list[0] == '2' :
            print('Lift is going up!')
            print('---------------')
            print('Lift has reached the 2nd floor!')
            print('---------------')
        elif floor_list[0] == '3' :
            print('Lift is going up!')
            print('---------------')
            print('Lift has reached the 3rd floor!')
            print('---------------')
        elif floor_list[0] == '4' :
            print('Lift is going up!')
            print('---------------')
            print('Lift has reached the 4th floor!')
            print('---------------')
        elif floor_list[0] == '5' :
            print('Lift is going up!')
            print('---------------')
            print('Lift has reached the 5th floor!')
            print('---------------')
        floor_list.pop(0)



