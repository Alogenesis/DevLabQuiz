'''
ทำการแบ่งประโยคจากคำที่กำหนดให้ โดยให้แบ่งขึ้นบรรทัดใหม่ทุกครั้งที่แบ่ง
บรรทัดแรก ประโยคหลักที่ต้องการแบ่ง
บรรทัดสอง คำที่ต้องการใช้แบ่งประโยค

This is very easy testcase.
a (ใช้ a แบ่ง)

Devices have been used to aid computation for thousands of years.
i (ใช้ i แบ่ง)
'''

user_input = input()
sepper = input()
sep = user_input.split(sepper)
print(sep)

for i in range(0,len(sep)-1):
    sep[i] = sep[i] + sepper
print(sep)

for i in sep:
    print(i)

for i in range(1,len(sep)):
    sep[i] = sepper + sep[i]

print(sep)