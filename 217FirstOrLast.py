'''
มีนักเรียน 2 คนกำลังแข่งกันว่าใครหาชื่อตัวเองเจอในใบรายชื่อก่อน แต่เนื่องจากพวกเขาหาชื่อได้เร็วมากจนสายตามนุษย์มองตามไม่ทัน
กรรมการเลยนึกโจทย์ในการเขียนโปรแกรมขึ้นมาได้ว่า ให้เขียนโปรแกรมที่ให้แสดงว่าเจอชื่อใครในรายชื่อก่อน
โดยที่ใบรายชื่อจะแสดงเป็นลำดับ a-z และโปรแกรมนี้สามารถเลือกได้ว่าหาจากท้ายขึ้นมาหน้าหรือหน้ามาหลัง (“first” หรือ “last”)
'''

lst = []
x = input()
y = input()
c = input()
lst.append(x)
lst.append(y)
lst.sort()

if c == 'first':
    print(lst[0])
else:
    print(lst[1])