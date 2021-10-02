'''
เรามีตัวเลขอยู่จำนวนหนึ่งโดยที่ เราอยากจะทราบว่า มันมีตัวเลขไหนบ้างนะที่ มันรวมกันเเล้วจะได้ ตัวเลขจำนวนเต็มที่เราต้องการหา
บรรทัดที่ 1 รับตัวเลขจำนวนเต็มที่เก็บเป็น list
บรรทัดที่ 2 ตัวเลขจำนวนเต็มที่เป็น Target
Index ที่รวมกันเเล้วได้ Target
In:
[1,2,3,4] str
5
Out:
2 1
3 0
'''

x = input()
y = int(input())
a1 = x.replace('[','')
a2 = a1.replace(']','')
lib_list_str = a2.split(',')
lib_list = []
for g in lib_list_str:
    lib_list.append(int(g))

i_index_count = 0
n_index_count = 0

answer_list = []
for i in lib_list:
    for n in lib_list:
        if (n + i) == y :
            print('i + n = 5',i,n,'index =',i_index_count,n_index_count)
            answer_list.append(i_index_count)
            answer_list.append(n_index_count)
            print(answer_list)
            n_index_count += 1
        else:
            print('i + n != 5',i,n,'index =',i_index_count,n_index_count)
            n_index_count += 1
    i_index_count += 1
    n_index_count = 0
print(answer_list)
len_answer_list = len(answer_list)
las_list = len_answer_list / 2
set_a = []
set_b = []
las_i = 0
las_n = 1
while las_list != 0:
    set_a.append(answer_list[las_i])
    set_b.append(answer_list[las_n])
    las_i += 2
    las_n += 2
    las_list -= 1

print(set_a,set_b)

last_answer = []
for i in range(0,4):
    if set_b[i] >= set_a[i]:
        last_answer.append(set_a[i])
        last_answer.append(set_b[i])
    else:
        pass




print(last_answer)
print(len(last_answer) / 2)
counter = (len(last_answer) / 2)
an = 0
bn = 1
while counter != 0:
    print(last_answer[bn],last_answer[an])
    an += 2
    bn += 2
    counter -= 1
