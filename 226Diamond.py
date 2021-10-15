'''
สร้างสี่เหลี่ยมข้าวหลามตัด
>> 5
  *
 ***
*****
 ***
  *
'''

x = int(input())
length = (x + 1)/2  #3
space = x - int(length)
dot = 1
lst = []

for i in range(0,int(length)):
    x = ' '*space + '*'*dot
    space -= 1
    dot += 2
    lst.append(x)
#print(lst)

for i in lst:
    print(i)

lst.reverse()
for i in lst[1:]:
    print(i)
