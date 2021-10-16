# Situation 1
'''
a_line = 2
a_column = 2
b_line = 2
b_column = 3
a = [[1, 2],        # 2 x 2   (Row x Col)
     [3, 4]]

b = [[5, 6, 7],     # 2 x 3
     [8, 9, 10]]
'''

# Situation 2
a_line = 3
a_column = 3
b_line = 3
b_column = 2
a = [[1, 3, 4],        # 3 x 3 (Row x Col)
     [3, 2, 2],
     [1, 2, 3]]

b = [[1, 2],        # 3 x 2
     [3, 4],
     [5, 6]]
# matrix ใหม่  = A นอน B ตั้ง   =  3 x 2
bp = b


'''     
A run ได้ตามค่า A คือ 2 ครั้ง 0 1
B run ได้ 3 ครั้ง คือ 0 1 2
บรรทัด 2 ของอันใหม่เกิดจาก line A มี 2 (Row A)
ต่อแถวมี 3 มาจาก หลัก B (Column B)

'''

'''
situation 1
2 x 3 Rol Col
00*00 + 01*10       00*01 + 01*11        00*02 + 01*12
10*00 + 11*10       10*01 + 11*11        10*02 + 11*22

situation 2
3 x 2 Row Col
00*00 + 01*10 + 02*20        00*01 + 01*11 + 02*21

'''

print('a =', a)
print('b =', b)



lst = []

for k in range(0,a_line): #เปลี่ยนตัวหน้า A เท่าจำนวนบรรทัดของ A (สุดท้ายเลย)
    for j in range(0,b_column): #Run เปลี่ยน B ที่ท้าย
        # ans at 00
        for i in range(0,a_column):
            result = a[k][i]*b[i][j]
            lst.append(result)

print(lst)


# บวกเลข x จำนวน แล้วให้เป็น 1 ตำแหน่งของ last matrix
forpop_lst = lst
mat_sum = []
while len(forpop_lst) > 0 :
    #start
    sum_lst = 0
    for i in range(0,a_column):  # กี่ตัวบวกกันถึงจะได้ 1 ค่า ดูจากว่า A ที่ชนมีกี่อัน == a_col
        sum_lst += forpop_lst[i]
    mat_sum.append(sum_lst)

    for i in range(0,a_column): # pop ทิ้งเท่ากับตัวที่บวกไปแล้ว
        forpop_lst.pop(0)
print(mat_sum)




# จัดเรียง Matrix
new_matrix = []
complex_matrix = []
while len(mat_sum) > 0:
    # Add เลขหน้า 2 ครั้ง  = จำนวน b ค่า  (ใหม่ = A นอน B ตั้ง)
    for i in range(0,b_column) : # 2 คือ เลขค่า
        new_matrix.append(mat_sum[i])
    # Pop เลขหน้าทิ้ง 2 ครั้ง
    for i in range(0,b_column) : # 2 คือ เลขค่า
        mat_sum.pop(0)

    complex_matrix.append(new_matrix)
    new_matrix = []
print(complex_matrix)

for i in complex_matrix:
    print('[',end='')
    print(*i,end='')
    print(']')


