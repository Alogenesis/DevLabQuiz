'''
โจทย์
จงสร้างฟังก์ชั่น ที่รับค่า string และ number
หากจำนวนตัวอักษร มีมากกว่าค่า number ให้พิมพ์ "..." ต่อท้ายตัวอักษร
แต่ถ้าหากจำนวนตัวอักษร มีน้อยกว่าค่า number ให้แสดงตัวอักษรนั้นเลย
ตัวอย่าง
"NongJoy and friend shop" 4 => "Nong..."
"NongJoy and friend shop" 11 => "NongJoy and..."
"NongJoy" 20 => "NongJoy"
'''

txt = input()
number = int(input())

if len(txt) > number:
    print(len(txt),number)
    print(txt[0:(number)]+'...')
else:
    print(txt)