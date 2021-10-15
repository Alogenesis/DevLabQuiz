a_line = 5
a_column = 5
b_line = 5
b_column = 5


for f in range(0,a_line):
    # Algirhythm for 1 line
    first = []
    for n in range(0, a_line):  # รัน A01 A02 A0n
        for i in range(0,b_column): #ที่ A00 ลองคูณกับทุก B0x แล้วเก็บค่า
            print('i = {} , n = {} , f = {}'.format(i,n,f))