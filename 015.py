'''
รับข้อมูลแล้วแสดงคำตอบกลับ
Input : Sommai MeeMakMai
1950
Output : Welcome Sommai MeeMakMai to NongGipsy Pub
'''

name = input('What your name? ')
year = int(input('Birth year? '))
if year > 2003 :
  print('You shall not pass!')
else :
  print('Welcome', name , 'to NongGipsy Pub')