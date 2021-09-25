'''สร้าง pyramid หน้าตาแบบนี้
input : 4
   *
  ***
 *****
*******
 *****
  ***
   *
'''

user_input = int(input('>> '))

#Top
row = user_input
last_row = user_input +1
repeat = user_input -1

star = 1
space = user_input-1
for k in range(0,row):
    print( (" "*(space))  +  ("*"*star) )
    star += 2
    space -= 1

row = user_input -1
c_star = star - 4
c_space = space +2
for k in range(0,row):
    print( (" "*(c_space))  +  ("*"*c_star) )
    c_star -= 2
    c_space += 1