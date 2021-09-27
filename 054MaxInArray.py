'''
หาค่าสูงสุดใน list
'''
import re
a = input()
b = re.findall(r'\d+', a) #หาเฉพาะตัวเลขเอาเข้า list
b.sort() #เรียงจากน้อยไปมาก
print(b[-1]) #ปริ้นตัวหลังสุด ค่ามากสุด
