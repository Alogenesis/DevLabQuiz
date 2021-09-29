'''
ทำสูตรคูณ
รับค่าเเม่สูตรคูณเสร็จเเล้วให้ทำออกมาเป็นเเม่สูตรคูณ เช่น
input
2
output
2 x 1 = 2
2 x 2 = 4
ไปเรื่อยๆจนถึง
2 x 12 = 24
นำมารวมกันได้ 154
ปล.ตรงรวมคือ (2+4+6+8+...+24)=154
'''

x = int(input())
sum = 0
for i in range (1,13):
    print(x,'x',i,'=', (x*i))
    sum = sum + (x*i)
#sum_point_two = '{:.2f}'.format(sum)
print('รวม :','{:,.2f}'.format(sum))


'''
import locale
from decimal import Decimal

def f(d):
    return '{0:n}'.format(d)


locale.setlocale(locale.LC_ALL, 'en_us')
#print(f(Decimal(sum_point_two)))
print('รวม :',f(Decimal(sum_point_two)))
'''


