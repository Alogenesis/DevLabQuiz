'''
จงสร้างพีระมิดในรูปแบบง่ายๆดังนี้
Input 4
Output
*
**
***
****
'''

user_input = int(input('Type Number '))

for i in range(user_input):
  print('*' * (i+1))