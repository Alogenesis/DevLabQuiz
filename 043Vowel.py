'''
ในการคัดแยกพัสดุในการส่งสินค้าจะต้องทำการหาสินค้าที่ต้องการออกมาเพื่อทำการส่งให้กับลูกค้า
โดยเราจะต้องเขียนโปรแกรมที่ใช้ในการหาว่าสินค้าที่ต้องการอยู่ตำแหน่งใด!
โดยพนักงานจะใส่จำนวนของสินค้าทั้งหมด n จำนวน
แล้วทำการใส่รหัสของพัสดุลงไปตามจำนวน n
หลังจากนั้นจึงทำการใส่เลขพัสดุที่ต้องการหาเป็นอย่างสุดท้าย

รูปเเบบ Input
บรรทัดแรก n เป็นจำนวนของสินค้าทั้งหมด
บรรทัด n ต่อไป เป็นรหัสสินค้าเป็นเลขจำนวนเต็ม
บรรทัดสุดท้ายเป็นรหัสสินค้าที่ต้องการหา เป็นเลขจำนวนเต็ม
In :
10 (จำนวนสินค้าทั้งหมด)
1 (รหัสสินค้า)
3 (รหัสสินค้าที่ต้องการหา)
7
4
9
5
1
3
1
5
1

Out :
Position: 1,7,9
'''


for i in x:
  if i in vowel:
    pass
  else:
    out.append(i)
#print(out)
for i in out:
	print(i, end='')