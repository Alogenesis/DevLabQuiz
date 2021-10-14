
lst = ['a','b','c','d','e','f']

sep_lst =[]
while len(lst) > 0:
    for i in range(0,2):    #กี่ค่าต่อ 1 บรรทัด
        sep_lst.append(lst[i])
    lst.pop(0)

print(sep_lst)
print('[', end='')
print(*sep_lst, end='')
print(']')