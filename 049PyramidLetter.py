'''
สร้าง pyramid จากตัวอักษรตามแบบ
Python
          P
        y P y
      t y P y t
    h t y P y t h
  o h t y P y t h o
n o h t y P y t h o n  (ตรงกลางคือตัวแรก เรียงไปขวา ทางซ้ายคืออ่านกลับหลัง)
BORNTODEV
                B
              O B O
            R O B O R
          N R O B O R N
        T N R O B O R N T
      O T N R O B O R N T O
    D O T N R O B O R N T O D
  E D O T N R O B O R N T O D E
V E D O T N R O B O R N T O D E V

RePeAtEr
              R
            e R e
          P e R e P
        e P e R e P e
      A e P e R e P e A
    t A e P e R e P e A t
  E t A e P e R e P e A t E
r E t A e P e R e P e A t E r
'''

user_input = 'BORNTODEV' #input
sp_input = list(user_input)
print(sp_input)
rev_input = list(user_input)

rev_input.reverse()
print(rev_input)

rev_input.pop()
print(rev_input)
print(sp_input)

lib = rev_input + sp_input
print(lib)
print(*lib,sep=' ')

#blank replace
sumlib = []
lib1 = rev_input + sp_input
lib1.pop(0)
lib1.pop()
print(lib1)
print(lib)
print('-----------------------------------')

sumlib.append(lib)
sumlib.append(lib1)
print(sumlib)
print('-----------------------------------')
lib1.pop(0)
lib1.pop()
sumlib.append(lib1)
print(sumlib[0])
print(sumlib[1])
print(sumlib[2])
print('-----------------------------------')
#สร้างไว้หลายๆ lib
#sumlib = []

'''
for i in range(0,(int((len(lib1)/2) -1))):
    lib1[i] = ' '
    lib1.pop()
    sumlib[i].append(lib1)

for k in range(0,len(lib1)):
    print(sumlib[k])
'''

#ที่ต้องแทนที่
print((len(user_input))-1)
#print(*lib,sep=' ')

delete_char = len(user_input)-1

#Line 1
while delete_char > 0:
    lib = rev_input + sp_input
    for i in range(0,delete_char):
        lib.pop(0)
        lib.pop()
    print(' '*(delete_char*2),end='')
    print(*lib, sep=' ')
    delete_char = delete_char - 1

#last line
lib = rev_input + sp_input
print(*lib,sep=' ')
'''
lib = rev_input + sp_input
for i in range(0,7):
    lib.pop(0)
    lib.pop()
    print(*lib, sep=' ')
'''