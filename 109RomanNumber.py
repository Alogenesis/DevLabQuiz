'''
กฏของการเขียนเลขโรมัน คือ ห้ามเขียนตัวเดียวกันซ้ำมากกว่า 3 ครั้ง
ตัวอย่าง:
IIII = ❌
IV = ✅
โจทย์ จงเขียนโปรแกรมว่าเลขโรมันที่ ผู้ใช้งาน กรอกเข้าไปถูกต้องหรือไม่
หากถูกต้องให้แสดงผลคำว่า
'Correct'
หากไม่ถูกต้องให้แสดงผลคำว่า
'Not Correct'

แสดงผลคำว่า ผู้ใช้กรอกเลขโรมันได้ถูกต้องหรือไม่
'''

x = input()
if 'IIII' in x:
    print('Not Correct')
elif 'XXXX' in x:
    print('Not Correct')
else:
    print('Correct')