'''
ในระบบสุ่มของเกม ได้มีการกำหนดไว้ว่า จะทำการสุ่มไอเทมขึ้นมา 2 ชิ้น
จากนั้นผู้เล่นจะได้รับไอเทมชิ้นที่มีตัวอักษรนำหน้าที่มีลำดับก่อนหน้าเสมอ
แต่ถ้าผู้เล่นอยากได้อีกชิ้นด้วยจะต้องทำการจ่ายเงินเพิ่มด้วยคำว่า pay!
แต่ถ้าไม่อยากได้ไอเทมชิ้นที่ 2 จะเป็นการรับคำว่า enough
ให้เขียนโปรแกรมเพื่อหาว่าผู้เล่นได้ไอเทมอะไรในการสุ่มครั้งนั้น

บรรทัดที่ 1 : ชื่อไอเทมที่ถูกสุ่มมาชิ้นแรก
บรรทัดที่ 2 : ชื่อไอเทมที่ถูกสุ่มมาชิ้นที่ 2
บรรทัดที่ 3 : “pay!” หรือ “enough”

ไอเทมที่ได้รับ 1-2 บรรทัด โดยจะแสดงผลไอเทมที่มีตัวอักษรนำหน้าที่มีลำดับมากกว่าเสมอ
'''

ran1 = input()
ran2 = input()
dicision = input()

lst = []
lst.append(ran1)
lst.append(ran2)
lst.sort()

print(lst[0])
if dicision == 'pay!':
    print(lst[1])
else:
    pass