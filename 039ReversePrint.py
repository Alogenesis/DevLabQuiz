'''
คำอธิบาย
ให้ทำการเขียนโปรแกรมที่ทำการกลับด้านลำดับตัวหนังสือ ที่ทำการรับเข้ามา
รูปเเบบ Input
บรรทัดแรก ข้อความที่ต้องการกลับด้าน
รูปเเบบ Output
บรรทัดแรก ข้อความที่ทำการกลับด้านแล้ว
ข้อจำกัด
ข้อความที่รับเข้ามามีแค่ตัวหนังสือและเว้นวรค

BorntoDev > veDotnroB
ThisIsInput > tupnIsIsihT
abcdef > fedcba
'''

x = input('Insert a text >> ')
print(x[::-1])
