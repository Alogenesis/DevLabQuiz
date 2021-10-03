'''
กำหนดว่า
Good morning ใช้ได้ตอนเวลา 5:00 - 11:59
Good afternoon ใช้ได้ตอนเวลา 12:00 - 17:59
Good evening ใช้ได้ตอนเวลาหลัง 18:00 ขึ้นไป
In :
13:59
Sommai

Out :
Good afternoon, Sommai
'''

time_input = input()
name = input()

time_sep = time_input.split(':')
#print(time_sep)
timea = time_sep[0]
time = int(timea)

if time == 5 or time == 6 or time == 7 or time == 8 or time == 9 or time == 10 or time == 11:
    print('Good morning',end=', ')
elif time == 12 or time == 13 or time == 14 or time == 15 or time == 16 or time == 17:
    print('Good afternoon',end=', ')
else:
    print('Good evening',end=', ')

print(name)