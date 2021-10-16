'''
แยกตัวประกอบของ n เมื่อ n เป็นจำนวนเต็มที่มากกว่า 1
หากตัวเลขนั้นมีตัวประกอบที่ซ้ำกันเช่น 4 = 2 * 2 , 12 = 2 * 2 * 3 เป็นต้น
ให้แสดงในรูปเลขยกกำลังเช่น 12 = 2^2 * 3
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

ans_lst = []
pow_lst = []

while len(lib_factor) > 0 :
    pow_n = 1
    ans_lst.append(lib_factor[0])
    lib_factor.pop(0)

    while len(lib_factor) > 0 :
        if lib_factor[0] == ans_lst[-1] :
            print('เท่ากัน ยกกำลัง')
            pow_n += 1
            lib_factor.pop(0)
        else :
            break
    pow_lst.append(pow_n)
    pow_n = 1  #reset

print(ans_lst)
print(pow_lst)
print('left =',lib_factor)

#print answer

for i in range(0,len(ans_lst)-1):
    if pow_lst[i] == 1 :
        print(ans_lst[i],end=' ')
        print('*',end=' ')
    else:
        print(ans_lst[i], end='')
        print('^',end='')
        print(pow_lst[i],end=' ')
        print('*', end=' ')

#Last digit
if pow_lst[-1] == 1 :
    print(ans_lst[-1],end=' ')

else:
    print(ans_lst[-1], end='')
    print('^',end='')
    print(pow_lst[-1],end=' ')



