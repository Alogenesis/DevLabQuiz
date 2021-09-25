'''
ให้ทำการสร้างต้นคริสมาสต์จากความสูงที่รับเข้ามาโดยมีตัวอย่างดังภาพ
รูปเเบบ Input
บรรทัดแรก จำนวนเต็ม n เป็นความสูงของต้นคริสมาสต์
รูปเเบบ Output
แสดงต้นคริสมาสต์ตามความสูงที่รับเข้ามา
ข้อจำกัด
0<n<100
Input : 2
  *         1
 ***        3
  *         1
 ***        3
*****       5 (2x+1)
  |         3 (in+1)  center
==V==

Input : 3
   *        1
  ***       3 (2r)
   *        1
  ***       3
 *****      5 (3r)
   *        1
  ***       3
 *****      5
*******     7 (2x+1) (4r)
   |        4 (in+1) center
===V===
'''


'''     ช่วงกระดาษทดเลข 

user_input = int(input(">> "))
print('User input type =', type(user_input) , 'Value =', user_input) #execute

space = user_input+1
x = 0

#Show input = 2
#top
star = 1
print( (' '*(user_input+0))  +  ('*') )
#print('Space =', space)
#print('x =', x)
#print('Assign x = x+1')
star = star +2
print( (" "*(user_input-1))  +  ("*"*star) )

#middle
star = 1
print( (' '*(user_input+0))  +  ('*') )
star = star +2
print( (" "*(user_input-1))  +  ("*"*star) )
star = star +2
print( (" "*(user_input-2))  +  ("*"*star) )
#print( (" "*(user_input-1))  +  ("***") )
#print( (" "*(user_input-2))  +  ("*****") )

#bottom
print( (' '*(user_input+0))  +  ('/') )
print( ('='*(user_input-0)) + 'V' + ('='*user_input) )
'''




#Top
user_input = int(input(">> "))
star = 1
space = user_input
for a in range(0,2):
    print( (" "*(space))  +  ("*"*star) )
    star += 2
    space -= 1


#Middle Algorithm
row = 3
#value = 1
last_row = user_input +1
repeat = user_input -1


for j in range(0,repeat):
    # Value for print star
    star = 1
    space = user_input
    for k in range(0,row):
        print( (" "*(space))  +  ("*"*star) )
        star += 2
        space -= 1
        #value += 1
    row +=1
    #value = 1

#bottom
print( (' '*(user_input+0))  +  ('/') )
print( ('='*(user_input-0)) + 'V' + ('='*user_input) )