'''
ลำดับของตัวอักษร ถ้าเป็นคี่ ให้ตัวเล็ก  /  ถ้าเป็นคู่ให้เป็นใหญ่
python  >> pYtHoN
hippo  >>   hIpPo
tank  >>    tAnK
'''

x = input().lower()

for i in range(0,len(x)):
    #print(i,end=' ')
    #print(x[i])
    if i % 2 == 0:
        print(x[i].lower(),end='')
    else:
        print(x[i].upper(),end='')