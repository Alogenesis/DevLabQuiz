'''
ข้อความที่ได้รับ q T R K W G T
ลดตำแหน่งข้อความลงมาตามตำแหน่ง
ตำแหน่ง 1 2 3 4 5 6 7
ข้อความที่ได้ p R O G R A M
หลังจากนั้นสลับตำแหน่งจากใหญ่ไปเล็ก จากเล็กไปใหญ่
ข้อความที่ได้ P r o g r a m

concept = get > ascii > - char > to char > upper lower convert
'''

get = input()
print(get)

# sep char
char_lib = []
for i in get:
    char_lib.append(i)
print(char_lib)

# transfer to ascii
as_lib = []
for i in char_lib:
    as_lib.append(ord(i))
print(as_lib)

# minus char
encoder = 1
index = 0
for i in as_lib:
    as_lib[index] -= encoder
    encoder += 1
    index += 1
    print(i,encoder,'i,encoder,')
print(as_lib)

#ascii to char
new_char_lib = []
for i in as_lib:
    new_char_lib.append(chr(i))

print(new_char_lib)

for i in new_char_lib:
    if i.isupper():
        print(i.lower(),end='')
    elif i.islower():
        print(i.upper(),end='')
    else:
        print(i,end='')




