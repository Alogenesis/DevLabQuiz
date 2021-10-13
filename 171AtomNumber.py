'''
หลักการนับจำนวนอะตอม ของธาตุและสารประกอบ

1.นับแต่ตัวใหญ่ ตัวเล็กที่ห้อยมาช่วยเสริมไม่ให้ะาตุซำ้กันเฉยๆ
2.ถ้ามีเลขห้อยที่ตัวไหน ให้นับว่าตัวนั้นมีจำนวนตามเลขห้อย
EX. CaCO3 => Ca = 1 ตัว
             C = 1 ตัว
             O3 = 3 ตัว
             รวมเป็น 5 ตัว

EX. Na2CO3 => Na2 = 2 ตัว
              C = 1 ตัว
              O3 = 3 ตัว
              รวมเป็น 6 ตัว
EX. O3 => O3 = 3 ตัว
               รวมเป็น 3 ตัว

In :
NaCl
CaO
O2
Out :
2
2
2
'''

input_element = input()

element_lib = []

while len(input_element) > 0:
    if len(input_element) > 1 and input_element[1].islower():
        print('Go Small')
        element_lib.append(input_element[0:2])
        input_element = input_element.replace(input_element[0:2],'')

    elif input_element[0].isupper():
        element_lib.append(input_element[0])
        input_element = input_element.replace(input_element[0], '')
    elif input_element[0].isnumeric():
        if int(input_element[0]) == 2:
            element_lib.append(input_element[0])
        elif int(input_element[0]) == 3:
            element_lib.append(input_element[0])
            element_lib.append(input_element[0])
        elif int(input_element[0]) == 4:
            element_lib.append(input_element[0])
            element_lib.append(input_element[0])
            element_lib.append(input_element[0])
        input_element = input_element.replace(input_element[0],'')
    print(element_lib)
    print(input_element)




count = len(element_lib)
print(count)

