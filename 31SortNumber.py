'''
เรียงตัวเลขจากมากไปน้อย
'''

a = int(input('Type a number > '))
b = int(input('Type a number > '))
c = int(input('Type a number > '))
d = int(input('Type a number > '))
e = int(input('Type a number > '))

get = [a,b,c,d,e]
#print(get)
get.sort(reverse=True)
#print(get)

for i in get:
  print(i)