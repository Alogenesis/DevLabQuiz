'''
ใส่ input ลงไป 1 ค่า(integer) จากนั้นแยกตัวประกอบ
ของ input ให้แสดง output ออกมาเป็นในรูปของผลคูณของตัวประกอบ input,
โดยมีเงื่อนไขว่าตัวประกอบทุกตัวต้องเป็นจำนวนเฉพาะ
'''

num = int(input())
cnum = num
factor = [2,3,5] #if include factor for multiply are ugly number
                #Note 1 are ugly number exception
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
         113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
         181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
         251, 257, 263, 269, 271]

lib_factor = []
index = 0

while num not in prime:
    '''
    if num % 2 == 0:
        num = num / 2
        lib_factor.append(2)
    elif num % 3 == 0:
        num = num / 3
        lib_factor.append(3)
    elif num % 5 == 0:
        num = num / 5
        lib_factor.append(5)
'''
    for i in prime:
        if num % i == 0:
            print('Mod = 0')
            num = num / i
            lib_factor.append(i)
            break
        else:
            print('i =', i)
            print('Mod != 0')

# Add last prime
if num in prime:
    lib_factor.append(int(num))

# ได้ผลลัพท์เป็นตัวประกอบล่างสุดคือ มีแค่จำนวนเฉพาะ
print(lib_factor)
# เขียนได้ในรูป 2**n  3**n  5**n
for i in lib_factor:
    print(i)
