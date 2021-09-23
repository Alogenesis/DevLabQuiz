'''
จงสร้างพีระมิดในรูปแบบดังนี้ โดยดูตัวอย่างจากข้อมูลนำเข้า เพื่อให้ได้ผลลัพธ์ตามที่โจทย์ต้องการ
4
   *
  ***
 *****
*******
'''

myInput = int(input('Type number : '))
dot = '*'
space = ' '
maxSpace = myInput - 1
# 2x-1
for i in range(myInput):
  print( (space * maxSpace ) + (dot * (2*(i + 1)-1) ))
  maxSpace = maxSpace - 1