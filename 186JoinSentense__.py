'''
ให้ทำการเรียบเรียงประโยคที่กำหนดให้ออกมาเป็นประโยคเดียว
บรรทัดแรกจำนวนประโยค
บรรทัดที่เหลือ เป็นประโยคที่ต้องนำมารวมกัน


'''

x = 7 #int(input())
lst = [
'afraid of greatness.',
'Be not afraid',
'some achieve greatness,',
'greatness thrust upon them.',
'greatness. Some',
'Some are born great, some',
'greatness, and others have greatness',
]

'''
for i in range(0,x):
    y = input()
    lst.append(y)
'''

print(lst)
first_lst = []
rearrange_lst = []
dot = []
answer_lib = []

for i in lst:
    if i[0].isupper():
        first_lst.append(i)
    elif i[-1] != '.':
        rearrange_lst.append(i)
    elif i[-1] == '.' :
        dot.append(i)

print(first_lst)
print(rearrange_lst)
print(dot)

first1_spl = first_lst[0].split(' ')
print(first1_spl)

first2_spl = first_lst[1].split(' ')
print(first2_spl)

# Run หาประโยคแรก

print(first_lst[0])

# Algo run หาประโยคกลางมาต่อ
print('---------------------')
current = first_lst[0].split(' ')
print(current)
# Run หาประโยคต่อ
for i in range(0,len(rearrange_lst)):
    mid_spl = rearrange_lst[i].split(' ')
    print('ประโยคปัจจุบัน',mid_spl)
    if mid_spl[1] == current[-2] and mid_spl[0] == current[-1]:
        print('Same 2')
        print(rearrange_lst[i])
    elif mid_spl[0] == current[-1]:
        print('Same 1')
        print(rearrange_lst[i])
    else :
        print('No Same')

# Run หาประโยคท้าย
for i in range(0,len(dot)):
    dot_spl = dot[i].split(' ')
    print('ประโยคท้ายปัจจุบัน',dot_spl)
    if dot_spl[1] == current[-2] and dot_spl[0] == current[-1]:
        print('Same 2')
        print(dot[i])
    elif dot_spl[0] == current[-1]:
        print('Same 1')
        print(dot[i])
    else:
        print('No Same')







