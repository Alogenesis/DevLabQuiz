'''
โจทย์ คือ จงแสดงจำนวนตัวประกอบและ ตัวประกอบทั้งหมดของเลขN
In : 1000
Out : 16 : 1,2,4,5,8,10,20,25,40,50,100,125,200,250,500,1000
'''


'''
อธิบาย
ทุกตัวเลขที่ได้รับมาจะมีตัวประกอบ ที่มาจากจำนวน 1(พิเศษ) 2 3 5 และ ตัวมันเอง
คือ สามารถหารตัวเหล่านี้ลงตัว (% = 0) ยกตัวอย่างเช่น
15 หาร 2 ไม่ลงตัว ข้ามไป
15 หาร 3 ลงตัว ตัวประกอบ คือ 1 3 เหลือ 15/3 = 5
5 หาร 5 ลงตัว ตัวประกอบ คือ 1 3 5

14 หาร 2 ลงตัว ตัวประกอบ คือ 1 2
7 หาร 3 ไม่ลงตัว ข้ามไป
7 หาร 5 ไม่ลงตัว ข้ามไป
7 หาร 7 ลงตัว (ตัวมันเอง) สรุป เหลือ 1 2 7

ถ้าให้ระบุตัวประกอบทั้งหมด ของจำนวน ugly number ก็จะมีแค่ 2*i 3*i 4*i (i คือ จำนวนนับ 1 2 3 4 5)
แต่ถ้าไม่ใช่จำนวน ugly number ก็จะมีตัวท้ายเป็นจำนวนเฉพาะ
'''

num = 555 #int(input())
cnum = num
factor = [2,3,5] #if include factor for multiply are ugly number
                #Note 1 are ugly number exception
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
         113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
         181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
         251, 257, 263, 269, 271]

# 1. หา ตัวประกอบจำนวนเฉพาะของจำนวนนั้นให้ได้
# 1000 มีตัวประกอบเฉพาะ คือ 2 และ 3

prime_num = []
for i in factor:
    if num % i == 0:
        print('มีตัวประกอบเป็น', i)
        prime_num.append(i)
    else:
        print(i,'ไม่ใช่ตัวประกอบ')
print('จน.เฉพาะของ',num,'คือ',prime_num)

# 2. แยกตัวประกอบทั้้งหมดออกมาแต่ละตัวเป็นจำนวนเฉพาะ 2 3 5
lib_factor = []
while num not in prime:
    if num % 2 == 0:
        num = num / 2
        lib_factor.append(2)
    elif num % 3 == 0:
        num = num / 3
        lib_factor.append(3)
    elif num % 5 == 0:
        num = num / 5
        lib_factor.append(5)
    else: # append prime
        lib_factor.append(num)
# ได้ผลลัพท์เป็นตัวประกอบล่างสุดคือ มีแค่จำนวนเฉพาะ
lib_factor.append(int(num))
print(lib_factor)
# เขียนได้ในรูป 2**n  3**n  5**n


# 3. หาจำนวนตัวประกอบทังหมด ได้จาก เอาเลขยกกำลังบวก 1 เช่น
# 2**3 = 3+1  /  5**3 = 3+1
# รวม 4 x 4 = 16 ตัวประกอบทั้งหมด
# เขียนโปรแกรมให้หาตัวประกอบ โดยการเอาสมาชิกที่ซ้ำทั้งหมดมาเป็นเลขยกกำลัง

twopow = 0
threepow = 0
fivepow = 0
primepow = 0
for i in lib_factor:
    if i == 2:
        twopow += 1
    elif i == 3:
        threepow += 1
    elif i == 5:
        fivepow += 1
    else:
        primepow += 1

print('มีตัวประกอบทั้งหมด =',( (twopow+1) * (threepow+1) * (fivepow+1) * (primepow+1)) )
prime_factor = ( (twopow+1) * (threepow+1) * (fivepow+1) * (primepow+1) )

# 4. กระจายตัวประกอบ
extract_factor = [] #for loop
answer_factor = [] #for get answer
print(lib_factor)
#extract_factor.append(1)
answer_factor.append(1)
# append all lib_factor ไม่สนซ้ำ ลบทีหลัง
for i in lib_factor:
    extract_factor.append(int(i))  #ใช้ Loop
    answer_factor.append(int(i))

print('extract_factor =',extract_factor)

'''
คูณกันแบบ 1 index คูณกับตัวอื่นทั้งหมด
2x2
2x2x2
2x2x2x5
2x2x2x5x5
2x2x2x5x5x5
ลบตัวหน้า ลูปใหม่
2
2x2
2x2x5
2x2x5x5
2x2x5x5x5
ลบตัวหน้า ลูปใหม่
2
2x5
2x5x5
2x5x5x5
จนหมด
'''

sum_factor = 1
for i in extract_factor:
    for j in extract_factor:
        if i == j:
            pass
        else:
            sum_factor = i * j
            print(sum_factor)
            print('cnum = ',cnum)
            if sum_factor <= cnum :
                answer_factor.append(sum_factor)



while len(extract_factor) != 0:
    sum_factor = 1 # assign for sum
    for index in extract_factor:
        sum_factor = sum_factor * index
        answer_factor.append(sum_factor)

    extract_factor.pop(0)



print('answer_factor= ',answer_factor)

# Loop delete duplicate
mid_answer = []
for i in answer_factor:
    if i not in mid_answer:
        mid_answer.append(i)
mid_answer.sort()
print(mid_answer)

print(prime_factor,':',end=' ')
print(*mid_answer,sep=',')



