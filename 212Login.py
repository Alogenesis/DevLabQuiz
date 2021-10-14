'''
ตรวจเช็คว่า username และ password ที่ได้รับสามารถเข้าสู่ระบบได้หรือไม่ โดยที่ถูกต้องคือ
username = hello
password = 1212312121
'''

username = input()
password = input()

if username == 'hello' and password == '1212312121':
    print('Let’s GO!!!')
else:
    print('No No!!!')