'''
ณ ถนนแห่งหนึ่ง นาย A ซึ่งกำลังจะข้ามถนนเกิดความสงสัยขึ้นมาว่าอัตราเร็วของรถแต่ละคันเป็นเท่าไหร่
เขาจึงคิดหาวิธีการต่างๆ แต่ก็คิดไม่ออก จึงโทรไปหาคุณซึ่งเป็นโปรแกรมเมอร์ที่เก่งที่สุดในตำบล ให้ช่วยเขียนโปรแกรมคำนวณหาอัตราเร็วของรถบนถนน
ซึ่งนาย A ได้เลือกรถมาหนึ่งคันเพื่อหาว่ามีอัตราเร็วเท่าไหร่ โดยนาย A จะทำการจับเวลาที่รถเคลื่อนที่จากเสาไฟฟ้าต้นหนึ่งไปยังอีกต้นหนึ่ง
จากนั้นนาย A จะบอกเวลาที่ได้กับคุณ แล้วให้คุณหาอัตราเร็วของรถคันนั้น
(กำหนดให้ระยะห่างระหว่างเสาไฟฟ้า = 40 เมตร)
สูตรการหาอัตราเร็ว
อัตราเร็ว = ระยะทาง / เวลา
'''

s = 0.04 #km
sec = float(input('>>' ))
t = sec/3600
v = s/t


print('{0:.2f} km/hr'.format(v))