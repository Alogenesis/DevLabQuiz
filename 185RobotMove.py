'''
เราสร้าง หุ่นยนต์ ตัวหนึ่งให้เคลื่อนไปตาม input ที่เราป้อนให้
เริ่มต้นนั้นหุ่นยนต์จะหันหน้าไปทางแกน y ที่มีค่าบวก(เหนือ) เสมอ
แต่มันจะหันหน้าไปทาง แกน y ที่มีค่าลบ(ใต้) หรือ แกน x ที่มีค่าบวก(ตะวันออก) กับ แกน x ที่มีค่าลบ(ตะวันตก)
ตาม input ที่เราป้อนพร้อมกับเคลื่อนที่ไปหนึ่งหน่วย จนกว่า input นั้นจะเท่า กับ END ถึงจะหยุดการทำงาน

ปัญหาคือ เราควบคุมหุ่นยนต์ตัวนี้จากระยะไกล ทำให้เราหาตำแหน่งล่าสุดของหุ่นยนต์เพื่อไปตามเก็บค่อนข้างยาก
เราอยากให้พวกเธอช่วยคิดโปรแกรมที่แสดง ตำแหน่งล่าสุดของหุ่นยนต์ หลังจากจบการทำงานให้เราที

โดยก่อนเริ่มการทำงาน ที่บรรรทัดแรก จะต้องรับตำแหน่งหุ่นยนต์ ณ ปัจจุบัน เป็น (x,y) มาก่อน เช่น (0,0) หรือ (2,4) เป็นต้น
เริ่มต้นนั้นหุ่นยนต์จะหันหน้าไปทางแกน y ที่มีค่าบวก(เหนือ) เสมอ
บรรทัดถัดไปคือ การสั่งการให้ หุ่นยนเคลื่อนที่ ดังนี้
FW (เดินหน้า) หันไปทิศเดิม แล้วเคลื่อนที่ไปหนึ่งหน่วย
BK (ถอยหลัง) หันไปทิศตรงข้าม แล้วเคลื่อนที่ไปหนึ่งหน่วย
L ( เลี้ยวซ้าย) หันไปทางซ้าย แล้วเคลื่อนที่ไปหนึ่งหน่วย
R ( เลี้ยวขวา) หันไปทางขวา แล้วเคลื่อนที่ไปหนึ่งหน่วย
จนกว่า input จะเท่ากับ END ถึงจะหยุดการทำงาน

แสดง ตำแหน่งล่าสุดของหุ่นยนต์เป็น (x,y) เช่น (1,4) หรือ (2,3) เป็นต้น
'''

start = input()
edit_start = start.replace('(','')
edit = edit_start.replace(')','')
xstr,ystr = edit.split(',')
x = int(xstr)
y = int(ystr)
print(x,y)


front = 'up'

user_input = input()
while user_input != 'END' :

    if front == 'up' :
        if user_input == 'FW' :
            y += 1
            front = 'up'
        elif user_input == 'BK' :
            y -= 1
            front = 'down'
        elif user_input == 'L' :
            x -= 1
            front = 'left'
        elif user_input == 'R' :
            x += 1
            front = 'right'
        else:
            print('Error1')

    elif front == 'down' :
        if user_input == 'FW' :
            y -= 1
        elif user_input == 'BK' :
            y += 1
            front = 'up'
        elif user_input == 'L' :
            x += 1
            front = 'right'
        elif user_input == 'R' :
            x -= 1
            front = 'left'
        else:
            print('Error2')

    elif front == 'left' :
        if user_input == 'FW' :
            x -= 1
        elif user_input == 'BK' :
            x += 1
            front = 'right'
        elif user_input == 'L' :
            y -= 1
            front = 'down'
        elif user_input == 'R' :
            y += 1
            front = 'up'
        else:
            print('Error3')

    elif front == 'right' :
        if user_input == 'FW' :
            x += 1
        elif user_input == 'BK' :
            x -= 1
            front = 'left'
        elif user_input == 'L' :
            y += 1
            front = 'up'
        elif user_input == 'R' :
            y -= 1
            front = 'down'
        else:
            print('Error4')

    else:
        print('Error5')

    print(user_input)
    print(x, y)

    #Require input
    user_input = input()

#Answer
print('(',end='')
print(x,y,sep=',',end='')
print(')')