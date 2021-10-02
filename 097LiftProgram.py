'''
เราจะมีลิฟท์ทั้งหมด 5 ชั้น ได้แก่ 1 2 3 4 และ 5
และเราจะรับข้อมูลชั้นที่อยากจะไป
แล้วแสดงข้อมูลทีละ step โดย รูปแบบดูได้ที่ out put
ถ้ากรอกตัวเลขชั้นไม่ตรงกับที่มีอยู่ ให้ แสดง ว่า
Error! Not have this floor

output 1 step ต่อ 1 ทัด
รูปแบบคือ
OK! Wait please
---------------
Lift is arriving!
---------------
Lift is going up!
---------------
Lift has reached the (ชั้นตามด้วย *ตัวตามหลังอันดับ*) floor!
(-) 15 ตัว
ตัวตามหลังอันดับ เช่น 1st 2nd 3 rd 4th ...
ถ้ากรอกตัวเลขชั้นไม่ตรงกับที่มีอยู่ ให้ แสดง ว่า
Error! Not have this floor
แล้วจบ
'''

x = int(input())
if x <= 0:
    print('Error! Not have this floor')
elif x > 5:
    print('Error! Not have this floor')
else:
    print('OK! Wait please')
    print('---------------')
    print('Lift is arriving!')
    print('---------------')
    print('Lift is going up!')
    print('---------------')
    if x == 1:
        print('Lift has reached the 1st floor!')
    elif x == 2:
        print('Lift has reached the 2nd floor!')
    elif x == 3:
        print('Lift has reached the 3nd floor!')
    elif x == 4:
        print('Lift has reached the 4th floor!')
    else:
        print('Lift has reached the 5th floor!')



