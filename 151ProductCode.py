'''
ข้อนี้จะเป็นการบอกรายละเอียดสินค้าและนำมาคำนวณหาราคา รหัสก็จะมีมากมาย เช่น สี size และ อีกมากมาย โดยข้อนี้จะเป็น เสื้อผ้านะครับ
เราจะนำราคาทุกเงื่อนไขมาบวกกันจนได้ราคาสุทธิ
โดยจะมีเงื่อนไขทั้งหมดต่อไปนี้

บรรทัดที่ 1 - ประเภท
หมายเลข 1 คือ underwear(ชุดชั้นใน เช่น กางเกงใน และอื่นๆ) - ราคา 20
หมายเลข 2 คือ pants(กางเกง) - ราคา 30
หมายเลข 3 คือ skirt - ราคา 30
หมายเลข 4 คือ shirt - 40
หมายเลข 5 คือ blouse - 40

ด้านหลังคือราคานะครับ
ทีไม่ได้วงเล็บหาคำแปลกันเอาเองนะจ๊ะ
บรรทัดที่ 2 - size

หมายเลข 1 คือ S - 5
หมายเลข 2 คือ M - 10
หมายเลข 3 คือ L - 15
หมายเลข 4 คือ Xl -20
หมายเลข 5 คือ XXL - 25

ด้านหลังคือราคานะครับ
บรรทัดที่ 3 - สี

หมายเลข R คือ red - 15
หมายเลข B คือ blue - 15
หมายเลข W คือ white - 10
หมายเลข G คือ green - 15
หมายเลข BK คือ black - 15

ด้านหลังคือราคานะครับ
บรรทัดที่ 4 - เนื้อผ้า

หมายเลข 1 คือ cotton - 20
หมายเลข 2 คือ nylon - 15
หมายเลข 3 คือ spandex - 25
หมายเลข 4 คือ wool - 30
หมายเลข 5 คือ linen - 25

ด้านหลังคือราคานะครับ
บรรทัดที่ 5 - จำนวน

เป็นจำนวนเต็ม เช่น 1 2 3
ก็ให้นำราคาแต่ละเงื่อนไขมาบวกกัน แล้วมาคูณจำนวนนะครับ
'''

''' 
จะเขียนแบบใช้หลายครั้งก็ได้ 
เอาข้อมูลทั้งหมดใส่ List แล้วดึงมาใช้
แต่ในโจทย์นี้ใช้ครั้งเดียวแล้วรันใหม่
ดังนั้น ไถเอา
'''

product_type = int(input()) #รหัสสินค้า
size_code = int(input()) #รหัส size
color = input() #string รหัสสี
fabric_type = int(input()) #รหัสเนื้อผ้า
amout = int(input()) #จำนวนที่ซื้อ

# Create dict
p_type = {1:'underwear' , 2:'pants', 3:'skirt', 4:'shirt' , 5:'blouse'}
p_type_cost = {1:20 , 2:30, 3:30, 4:40 , 5:40}

s_code = { 1:'size S' , 2:'size M' , 3:'size L', 4:'size XL', 5:'size XXL'}
s_code_cost = {1:5 , 2:10 , 3:15 , 4:20 , 5:25}

color_trans = {'R':'color red', 'B':'color blue', 'W':'color white', 'G':'color green', 'BK':'color black'}
color_cost = {'R':15, 'B':15, 'W':10, 'G':15, 'BK':15}

fab_type = {1:'cotton', 2:'nylon', 3:'spandex' , 4:'wool', 5:'linen'}
fab_type_cost = {1:20, 2:15, 3:25 , 4:30, 5:25}


# calculate cost
product_cost = 0
# product type
product_cost += p_type_cost[product_type]
#size cost
product_cost += s_code_cost[size_code]
#color cost
product_cost += color_cost[color]
#Fabric Cost
product_cost += fab_type_cost[fabric_type]

#sum
print(product_cost)
# sum * amout
total = product_cost*amout
print(total)

# print bill
print(p_type[product_type],'-',p_type_cost[product_type])
print(s_code[size_code], '-' , s_code_cost[size_code])
print(color_trans[color], '-' , color_cost[color])
print(fab_type[fabric_type], '-' , fab_type_cost[fabric_type])
print('amount -', amout)
print('cost - ', product_cost ,'*',amout, ' = ', total , sep='' )