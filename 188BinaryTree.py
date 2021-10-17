loop = int(input())
lst = []
for i in range(0,loop):
    x = int(input())
    lst.append(x)



total_left = 0
total_right = 0
L_floor = 0
R_floor = 0
checker = lst[0]
if len(lst) >= 1:
    L_floor += 1
    R_floor += 1
    lst.pop(0)

print('main = ',checker)

less_lst = []
great_lst = []
for i in lst:
    if i < checker :
        total_left += 1
        L_floor += 1
        less_lst.append(i)
    else:
        total_right += 1
        R_floor += 1
        great_lst.append(i)


print('TL = ',total_left)
print(less_lst)
print('TR = ',total_right)
print(great_lst)
print(L_floor,'L_floor')
print(R_floor,'R_floor')

if loop > 1 :
    # Check less
    next_level = 0
    checker = less_lst[0]
    less_lst.pop(0)
    less_lst.sort()
    print(less_lst)
    left = 0
    right = 0
    for i in less_lst:
        if i < checker :
            left += 1
        else:
            right += 1

    if left == 0 or right == 0 :
        pass
    elif left == right :
        L_floor = L_floor/2
        R_floor = R_floor/2




#answer
print('floor=',L_floor,R_floor)

if L_floor == 0 :
    print(int(R_floor))
elif R_floor == 0 :
    print(int(L_floor))
elif L_floor == R_floor :
    print(int(L_floor))
elif L_floor == 1 or R_floor == 1:
    if R_floor > L_floor:
        print(R_floor)
    else:
        print(L_floor)
