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
a_column = int(aspl[1])      # ค่า A

bspl = b_get.split(' ')
b_line = int(bspl[0])        # แถว B
b_column = int(bspl[1])      # ค่า B


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

#Transpose B
max_tpline_b = b_column   #แถวตั้ง กลายเป็นแถวนอน   แถว
max_tpcolumn_b = b_line   #แถวนอน กลายเป็นแถวตั้ง   ค่า

#print('Here!! >', b_get_matrix[0][0], b_get_matrix[1][0], b_get_matrix[2][0])     #เอาตัวที่ 00 10 20 มา Testcode

b_tb_lip = []
#Loop Bruteforce
for j in range(0,max_tpline_b):

    # Loop transpose Column > Line
    loop_tp_lip = []
    for i in range(0,max_tpcolumn_b):
        x = b_get_matrix[i][j]
        loop_tp_lip.append(x)
    print(loop_tp_lip)
    b_tb_lip.append(loop_tp_lip)

print(b_tb_lip)

a = a_get_matrix
b = b_tb_lip

# จะคูณได้ไม่ได้ขึ้นอยู่กับว่า แนวนอนของ A == แนวตั้งของ B มั้ย
'''
a_dimension = [3,3]
b_dimension = [3,2]
a = [[1,3,4],
     [3,2,2],
     [1,2,3]]
b = [[1,2],
     [3,4],
     [5,6]]

b_prep = [[1,3,5],[2,4,6]]
'''


answer_matrix = []

for j in range(0,3): #run A0x A1x A2x
    # A0x run to 00 position
    po00 = 0
    for i in range(0,3):
        po00 += a[j][i]*b[0][i]
    print(po00)
    answer_matrix.append(po00)

    # A0x run to 01 position
    po01 = 0
    for i in range(0,3):
        po01 += a[j][i]*b[1][i]
    print(po01)
    answer_matrix.append(po01)

print(answer_matrix)

# เมตริกที่คูณกัน มิติใหม่ที่ได้ คือ Amp x Bpn = Cmn คือ แถวA(เลขหน้าA) คอลัมน์B(เลขหลังB)
# จากข้อนี้จะได้ 3 แถว 2 ค่า

# หาว่า print กี่ค่าต่อ 1 บรรทัด
n_val_inline = b_column  #n = เลขหลังของ B  n  = ค่าต่อบรรทัด
m_val_column = a_line    #m = เลขหน้าของ A  m  = บรรทัด


# Loop i in ans matrix




'''
จับ A ตะแคงตามเข็มแล้วพุ่งชน
ดูภาพวิธีคูณ จากเว็บนี้
https://nockacademy.com/math/math-%E0%B8%A1-4/
%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%9A%E0%B8%A7%E0%B8%81-%E0%B8%A5%E0%B8%9A
-%E0%B9%81%E0%B8%A5%E0%B8%B0%E0%B8%84%E0%B8%B9%E0%B8%93%E0%B9%80%E0%B8%A1%
E0%B8%97%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%8B%E0%B9%8C/
'''

