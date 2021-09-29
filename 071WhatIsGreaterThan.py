'''
รับค่า input เป็น str รูปแบบ a==b
ปริ้นว่า a หรือ b มากกว่ากัน
'''

user_input = input()
x = user_input.split('==')
print(user_input)
print(type(user_input))
print(x)
print(type(x))

if int(x[0]) > int(x[1]):
    print(x[0])
else:
    print(x[1])
