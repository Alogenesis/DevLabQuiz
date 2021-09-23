'''
จงรับเลขจำนวนเต็ม มาทั้งหมดสองจำนวนเพื่อหาว่าจำนวนไหนมากกว่ากัน และ แสดงเป็นชื่อตัวแปรนั้นๆ ถ้ามีค่าเท่ากันให้แสดงเป็น "AB" บรรทัดแรกที่รับค่าคือตัวแปร A บรรทัดที่สองที่รับค่าคือตัวแปร B
'''
A = int(input('Type number '))
B = int(input('Type number '))
#Output of Input Example
#print(type(A))
#print(type(B))
if A > B :
	print('A')
elif B > A :
	print('B')
elif A == B :
  print('AB')