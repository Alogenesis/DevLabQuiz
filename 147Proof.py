'''
ตำรวจต้องการข้อมูลผู้ร้ายจากคุณเพราะคุณเป็นพยานในเหตุการณ์
คำตอบของคุณจะเป็น
T = true
F = false
DS = doesn't see

รูปเเบบ Input
ลักษณะ : ข้อมูล
ลักษณะที่ตำรวจถาม : ข้อมูล

รูปเเบบ Output
T/F/DS

hat color : red
hat color : red
>> T

glasses : have
glasses : doesn\'t have
>> F

hair : wavy
shoe : boot
'''

user_input = input()
police_input = input()
user = user_input.split(' : ')
print(user)


police = police_input.split(' : ')
print(police)

if user == police : #ตรงกันหมด
    print('T')
elif user[0] == police[0] and user[1] != police[1]: #ตรงเฉพาะคำถาม
    print('F')
else:
    print('DS')
