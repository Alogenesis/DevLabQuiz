'''
ในการเล่นปาเป้าอย่างง่าย ผู้เล่นจะต้องปาเป้า ให้แต้ม n ลดลงเรื่อยๆจนหมด ซึ่งแผ่นเป้านั้นจะประกอบไปด้วยวงกลมซ้อนกันเป็นชั้นๆ
โดยวงที่อยู่ในสุดจะมีคะแนนถึง 5 คะแนน และ
วงข้างนอกก็จะมีคะแนนลดลงไปเรื่อยๆ จนเหลือ 0 (ปาไม่โดนเป้า)
นาย X เป็นนักกีฬามือโปร เขามีความแม่นยำมากสามารถปาลงจุดใดของแผ่นเป้าก็ได้
แต่ถึงอย่างงั้น เขาก็ยังจำเป็นต้องมีคุณเพื่อให้คุณช่วยในการคำนวณลูกดอกที่ต้องใช้
คุณจำเป็นต้องช่วยเขาคิดว่าเขาต้องใช้ลูกดอกอย่างน้อยกี่ดอกเพื่อให้สามารถปาจนแต้มหมดลงพอดี
ตัวอย่าง
n = 10
นาย X จำเป็นต้องใช้ลูกดอกอย่างน้อย 2 ดอก กล่าวคือ นาย X จะปาลงช่องที่มี 5 คะแนน ถึง 2 ครั้ง (5+5=10)

In : 10 / 13 / 27
Out : 2 / 3  / 6
'''

import math

n = 100
left = n

if n > 1000000000:
    print(math.ceil(n/5))
else:
    count = 1
    while n > 5:
        if n > 5 :
            count += 1
            n = n - 5
            #print(count)
            #print(n)
        elif n <= 5 :
            count += 1
            #print(count)
    #print('----------------')
    print(count)
    #print('================')

roundup