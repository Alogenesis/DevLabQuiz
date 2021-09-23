'''
1. ปีที่หารด้วย 4 ลงตัวจะเป็นปีอธิกสุรทิน
2. ปีที่หารด้วย 100 ลงตัวจะเป็นและไม่เป็นปีอธิกสุรทิน
3. ปีที่หารด้วย 400 ลงตัวจะเป็นปีอธิกสุรทิน
'''

year = int(input())
if year % 400 == 0 :
  print('Leap Year')
elif year % 100 == 0 :
  print('Not a Leap Year')
else :
  if year % 4 == 0 :
    print('Leap Year')
  else :
    print('Not a Leap Year')