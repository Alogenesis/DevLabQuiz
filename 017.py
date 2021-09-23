'''พีระมิดเท่าตัวเลขที่ได้รับ
Input : 5
Out :
*
**
***
****
*****
'''
myInput = int(input('Type a number : '))
for i in range(myInput):
  print( '*' * (i + 1 ) )