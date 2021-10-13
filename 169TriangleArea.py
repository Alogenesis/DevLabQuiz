'''
จงคำนวนพื้นที่ 3 เหลี่ยม
สุตร: 1/2 * ฐาน * สุง
In :
บรรทัดที่ 1 ความยาวฐาน
บรรทัดที่ 2 ความสูง
Out :
10.5 cm2
'''

long = int(input())
high = int(input())

area = (long * high) / 2

if area - int(area) == 0:
    print(int(area), 'cm2')
else:
    print(area, 'cm2')



