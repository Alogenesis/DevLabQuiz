'''
เรียงเลขเท่าที่รับมา
In : 5 //บรรทัดแรกสุดจะเอาไว้บอกว่าจะรับข้อมูลทั้งหมดกี่ตัว
3
5
1
2
9

Out :
9
5
3
2
1
'''

getRange = int(input())
lib = []
for i in range(getRange):
    a = int(input())
    lib.append(a)
    # print(lib)

lib.sort(reverse=True)
# print(lib)

for i in lib:
    print(i)