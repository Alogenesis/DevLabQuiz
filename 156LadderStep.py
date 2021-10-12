'''
ทำการสร้างบันไดตามจำนวนขั้นบันไดที่รับเข้ามา
3
         __
      __|
   __|
__|

0
__

10
                              __
                           __|
                        __|
                     __|
                  __|
               __|
            __|
         __|
      __|
   __|
__|
'''

num_input = int(input())
#print('--')
space = '   '
first_space = num_input
print(space*(first_space),'__',sep='')
for i in reversed(range(0,num_input)):
    print(space*i,end='')
    print('__|')

