'''
ในการคัดแยกพัสดุในการส่งสินค้าจะต้องทำการหาสินค้าที่ต้องการออกมาเพื่อทำการส่งให้กับลูกค้า โดนเราจะต้องเขียนโปรแกรมที่ใช้ในการหาว่าสินค้าที่ต้องการอยู่ตำแหน่งใด!
โดยพนักงานจะใส่จำนวนของสินค้าทั้งหมด n จำนวน แล้วทำการใส่รหัสของพัสดุลงไปตามจำนวน n หลังจากนั้นจึงทำการใส่เลขพัสดุที่ต้องการหาเป็นอย่างสุดท้าย

บรรทัดแรก n เป็นจำนวนของสินค้าทั้งหมด
บรรทัด n ต่อไป เป็นรหัสสินค้าเป็นเลขจำนวนเต็ม (เลขรัวๆ)
บรรทัดสุดท้ายเป็นรหัสสินค้าที่ต้องการหา เป็นเลขจำนวนเต็ม (เลขที่ต้องการ ให้หาว่าอยู่บรรทัดไหนบ้าง)

In :
5 (รับค่าแรก จำนวนสินค้าทั้งหมด)
1 (เลขพัสดุ รัวๆ
2
1
2
1 จบ )
1 (เลขที่ต้องการหา)

Out : Position: 1,3,5
'''

#Input total Goods
total_goods = int(input(' Total Goods? >> '))

#Input Goods code
code = []
for i in range(0,total_goods):
    x = int(input('Code > '))
    code.append(x)

#Input finder code
finder = int(input('Finder Code > '))
index = []
for i in range(0,total_goods):
    if code[i] == finder:
        index.append(i+1)
    #print(code[i])
    #print(i)
    #print('----')
    #append index +1


print('Position: ',end='') #join line
print(*index, sep=',') #unpack