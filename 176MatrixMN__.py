'''
ให้ทำการคูณเมทริกซ์ 2 เมทริกซ์ มิติ m × n ตามที่โจทย์ระบุให้
บรรทัดที่ 1 รับจำนวนเต็มบวก 2 จำนวน แสดงมิติของเมทริกซ์ A
บรรทัดที่ 2 รับจำนวนเต็มบวก 2 จำนวน แสดงมิติของเมทริกซ์ B
บรรทัดที่ 3 ถึง mA+2 รับจำนวนเต็มบวก nA จำนวนในแต่ละบรรทัด
บรรทัดที่ mA+3 ถึง mA+(mB+2) รับจำนวนเต็มบวก nB จำนวนในแต่ละบรรทัด

รูปเเบบ Output
แต่ละบรรทัดแสดงสมาชิกของเมทริกซ์ผลลัพธ์ AB
ถ้าเมทริกซ์ทั้ง 2 ไม่สามารถคูณกันได้ให้แสดง output เป็น "Cant calculate !"

3 3         (A Dimension) (3 บรรทัด 3 ค่า)
3 2         (B Dimension)  (3 บรรทัด 2 ค่า)
1 3 4       ของ A 1
3 2 2       ของ A 2
1 2 3       ของ A 3
1 2         ของ B 1
3 4
5 6
'''
#Input management
a_get = input()
b_get = input()

aspl = a_get.split(' ')
a_line = int(aspl[0])        # แถว A
a_column = int(aspl[1])      # ค่า A หลัก

bspl = b_get.split(' ')
b_line = int(bspl[0])        # แถว B
b_column = int(bspl[1])      # ค่า B หลัก


#for loop get All A
a_get_matrix = []
for i in range(0,a_line):
    x_get = input()
    xspl = x_get.split(' ')
    print(xspl)
    #loop for str to int
    int_a_lib = []
    for i in xspl:
        int_a_lib.append(int(i))
    print(int_a_lib)
    a_get_matrix.append(int_a_lib)

print(a_get_matrix)



#for loop get All B
b_get_matrix = []
for i in range(0,b_line):
    x_get = input()
    xspl = x_get.split(' ')
    print(xspl)
    #loop for str to int
    int_b_lib = []
    for i in xspl:
        int_b_lib.append(int(i))
    print(int_b_lib)
    b_get_matrix.append(int_b_lib)

print(b_get_matrix)     #ค่า b matrix

a = a_get_matrix
b = b_get_matrix

# จะคูณได้ไม่ได้ขึ้นอยู่กับว่า จำนวนตั้งของ A == จำนวนบรรทัดของ B มั้ย
if a_column != b_line:  # ถ้าแนวนอน A ไม่เท่ากับ B คูณไม่ได้
    print('Cant calculate !')
else:  # ถ้าคูณได้

    lst = []

    for k in range(0, a_line):  # เปลี่ยนตัวหน้า A เท่าจำนวนบรรทัดของ A (สุดท้ายเลย)
        for j in range(0, b_column):  # Run เปลี่ยน B ที่ท้าย
            # ans at 00
            for i in range(0, a_column):
                result = a[k][i] * b[i][j]
                lst.append(result)

    print(lst)

    # บวกเลข x จำนวน แล้วให้เป็น 1 ตำแหน่งของ last matrix
    forpop_lst = lst
    mat_sum = []
    while len(forpop_lst) > 0:
        # start
        sum_lst = 0
        for i in range(0, a_column):  # กี่ตัวบวกกันถึงจะได้ 1 ค่า ดูจากว่า A ที่ชนมีกี่อัน == a_col
            sum_lst += forpop_lst[i]
        mat_sum.append(sum_lst)

        for i in range(0, a_column):  # pop ทิ้งเท่ากับตัวที่บวกไปแล้ว
            forpop_lst.pop(0)
    print(mat_sum)

    # จัดเรียง Matrix
    new_matrix = []
    complex_matrix = []
    while len(mat_sum) > 0:
        # Add เลขหน้า 2 ครั้ง  = จำนวน b ค่า  (ใหม่ = A นอน B ตั้ง)
        for i in range(0, b_column):  # 2 คือ เลขค่า
            new_matrix.append(mat_sum[i])
        # Pop เลขหน้าทิ้ง 2 ครั้ง
        for i in range(0, b_column):  # 2 คือ เลขค่า
            mat_sum.pop(0)

        complex_matrix.append(new_matrix)
        new_matrix = []
    print(complex_matrix)

    for i in complex_matrix:
        print('[', end='')
        print(*i, end='')
        print(']')



'''
จับ A ตะแคงตามเข็มแล้วพุ่งชน
ดูภาพวิธีคูณ จากเว็บนี้
https://nockacademy.com/math/math-%E0%B8%A1-4/
%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A7%E0%B8%81-%E0%B8%A5%E0%B8%9A
-%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%84%E0%B8%B9%E0%B8%93%E0%B9%80%E0%B8%A1%
E0%B8%97%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%8B%E0%B9%8C/
'''

