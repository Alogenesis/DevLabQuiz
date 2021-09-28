'''
จงคำนวณหาค่า 2^2+4^2+6^2+…+n2 โดยที่ค่า n คือ input ที่ได้รับ
'''

pow = 2
n = int(input())
sum = 0
all_sum = 0

for i in range(2,n+1,2):
    print('I = ',i)
    print(i,'**2 =', i**2)
    sum = i ** 2
    print(sum)
    count += 2
    all_sum = all_sum + sum
    print('--Code--')

print(all_sum)