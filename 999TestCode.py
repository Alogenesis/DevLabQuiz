user_input = 4 #int(input())
lst = [
'the day, thou canst not then be false to any man.',
'This above all: to thine own self',
'must follow, as the night the day, thou',
'own self be true, and it must follow, as',
]

'''
for i in range(0,x):
    y = input()
    lst.append(y)
'''
# input management
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

print('first_lst =', first_lst)
print('rearrange_lst =',rearrange_lst)
print('dot =', dot)

# add list member to main list
first_main_lst = []
for i in first_lst :
    x = i.split(' ')
    first_main_lst.append(x)

mid_main_pop = []
mid_main_lst = [] #Add ทั้งหมดลง mid
for i in first_lst : #Add first ไปใน mid
    x = i.split(' ')
    mid_main_lst.append(x)
    mid_main_pop.append(x)


for i in rearrange_lst :    #Add mid ลง mid
    x = i.split(' ')
    mid_main_lst.append(x)
    mid_main_pop.append(x)

#last add to mid
for i in dot :
    x = i.split(' ')
    mid_main_lst.append(x)
    mid_main_pop.append(x)

print(first_main_lst)
print(mid_main_lst)


#Algorhytm
countlst = user_input
mainlst = []
sublst =  []


# Add main list
mainlst.append(mid_main_lst[0]) # add ประโยคแรกลงไป
countlst -= 1
sublst.append(mid_main_lst[0]) # sub list ไว้เช็ค
current_checker = mid_main_lst[0] #'ไว้สำหรับเช็ค'
mid_main_lst.pop(0)
print('current_checker =',current_checker)
print('เหลือ', mid_main_lst)
print('เหลือกี่ประโยคที่ต้องใส่ =',countlst)
#mid_main_lst.append(x)
#mid_main_pop.append(x)

print('=== start Loop ===')

run = len(mid_main_lst)
while run > 0:

    unmatch = len(mid_main_lst)
    for i in mid_main_lst:

        print('checker = ', current_checker, 'i=',i , )
        #print('เช็ค 1 คำ', current_checker[-1], i[0])
        #print('เช็ค 2 คำ', current_checker[-2], i[1])

        if current_checker[-2] == i[0] and current_checker[-1] == i[1]:  # ท้าย2 เท่ากับต้น 2
            sublst.append(i)  # ลง sub ไว้เช็ค
            x = i  # ลบตัวหน้า 2 ตัว
            y = x[2:]
            mainlst.append(y)  # mid main ที่ i
            countlst -= 1
            current_checker = i
            print('เหมือน 2')
            print('main lst = ', mainlst)
            print('sub =', sublst)
            mid_main_lst.remove(i)
            print('เหลือ', mid_main_lst)

            break
        elif current_checker[-1] == i[0] :  # ท้าย1 เท่ากับต้น 1
            sublst.append(i)  # ลง sub ไว้เช็ค
            x = i  # ลบตัวหน้า 2 ตัว
            y = x[1:]
            mainlst.append(y)  # mid main ที่ i
            countlst -= 1
            current_checker = i
            print('เหมือน 1')
            print('main lst = ', mainlst)
            print('sub =', sublst)
            mid_main_pop.remove(i)
            mid_main_lst.remove(i)
            print('เหลือ', mid_main_lst)
            break
        elif current_checker[-3] == i[0]:
            sublst.append(i)  # ลง sub ไว้เช็ค
            x = i  # ลบตัวหน้า 2 ตัว
            y = x[3:]
            mainlst.append(y)  # mid main ที่ i
            countlst -= 1
            current_checker = i
            print('เหมือน 2')
            print('main lst = ', mainlst)
            print('sub =', sublst)
            mid_main_lst.remove(i)
            print('เหลือ', mid_main_lst)

        elif unmatch == 0 :
            break
        else:
            unmatch -= 1
            print('ไม่ตรง-1 เหลือ', unmatch)

    run -= 1






#answer
print('answer')
print(mainlst)
print(sublst)
print(countlst)
for i in mainlst :
    print(*i,end=' ')












