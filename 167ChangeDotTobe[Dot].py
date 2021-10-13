'''
เราจะทำการเปลียน IP address จากปกติที่เป็น 1.1.1.1 เป็น 1[.]1[.]1[.]1
คือเอา . ไปอยู่ใน []
'''

x = '127.0.0.1' #input()

lib = list(x)
print(lib)

lst = []
for i in lib:
    if i == '.':
        lst.append('[.]')
    else:
        lst.append(i)

print(*lst,sep='')
