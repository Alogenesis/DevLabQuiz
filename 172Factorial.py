'''
หาค่า Factorial จาก input ที่รับมาเป็น String
in : [5]
Out : 5!:120
'''

import math
get  = input()
get1 = get.replace('[','')
get2 = get1.replace(']','')
num = int(get2)
#print(num)
print('{}!:'.format(num),end='')
print(math.factorial(num))