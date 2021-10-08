'''
สร้างตัวแปรเก็บชื่อและรหัสผ่านสสำหรับสมัครสมาชิก
และสร้างตัวแปรเก็บชื่อและรหัสผ่านสำหรับล็อกอิน
หากรหัสผ่านไม่ตรงกันจะวนซ้ำไม่สิ้นสุด

name : Rati
password : 123456789
name(login) : Rati
password(login) : 123456789
Out : Success

name : Phoom
password : DEV123
name(login) : Phoom
password(login) : pjxhkxn
Out : Error
'''


user_name = input()
password = input()
log_user = input()
log_pass = input()

user_name = user_name[7:]
password = password[11:]
log_user = log_user[14:]
log_pass = log_pass[18:]

#print(user_name)
#print(password)
#print(log_user)
#print(log_pass)

if user_name == log_user and password == log_pass:
    print('Success')
elif user_name != log_user or password != log_pass:
    print('Error')
