'''
แม่ค้าขายผลไม้ ณ ย่านอารีย์ เห็นว่าคุณมีฝีมือในการเขียนโปรแกรมค่อนข้างมาก
จึงอยากวานให้คุณเขียนโปรแกรมหาจำนวนชนิดของผลไม้ในตระกร้าที่ลูกค้าประจำแต่ละคนซื้อ
และ หาว่าลูกค้าคนไหนซื้อผลไม้ต่างชนิดกันมากที่สุด เพื่อนำไปทำสถิติบางอย่าง

In : ผลไม้ทั้งหมดที่มีอยู่ในตระกร้าของนาย A, B และ C
A: apple orange grape orange B: mango mango grape C: banana banana
A: papaya apple B: watermelon coconut coconut C: pineapple strawberry strawberry avocado
A: cherry B: guava melon pear C: guava kiwi

Out : A  /  C  / B
'''

user_input = 'A: apple orange grape orange B: mango mango grape C: banana banana'
spl = user_input.split(' ')         #for cutting
spl_full = user_input.split(' ')    #maintain
print(spl)

a = []
b = []
c = []

al = []
bl = []
cl = []

pop_count = 0

spl = user_input.split(' ')  # for cutting
spl_full = user_input.split(' ')
for i in spl_full:
    if i == 'A:':
        spl.pop(0)
        pop_count += 1
    elif i == 'B:':
        break
    else:
        a.append(i)
        spl.pop(0)
        pop_count += 1

#print(a)    #check
#print(spl)  #check

# Remove duplicate
for j in a:
    if j not in al:
        al.append(j)
#print(al)  #check type of fruit in a member
#print(spl_full)

print('--------------------')
print('al =',al)
print('spl_f =', spl_full)
print('spl =', spl)
print('--------------------')

#create new spl with pop_count
print(pop_count,'Pop')
spl2 = user_input.split(' ')
for pop in range(0,pop_count):
    spl2.pop(0)
print('Now spl 2 =', spl2)

# Run to find B member
for k in spl2:
    #print('Now spl2 =', spl2)
    #print('Now spl =', spl)
    if k == 'B:':
        spl.pop(0)
        pop_count += 1
        #print('pop 0')
    elif k == 'C:':
        #print('break')
        break
    else:
        b.append(k)
        spl.pop(0)
        pop_count += 1
        #print('append i in b')
        #print('pop 0')

# Remove duplicate
for l in b:
    if l not in bl:
        bl.append(l)

print('--------------------')
print(bl)
print('--------------------')


#create new spl with pop_count
print(pop_count,'Pop')
spl3 = user_input.split(' ')
for pop in range(0,pop_count):
    spl3.pop(0)
print('Now spl 3 =', spl3)


for m in spl3:
    if m == 'C:':
        spl.pop(0)
    elif m == 'D:':
        break
    else:
        c.append(m)
        spl.pop(0)

# Remove duplicate
for nn in c:
    if nn not in cl:
        cl.append(nn)
print(cl)

a_mem = len(al)
b_mem = len(bl)
c_mem = len(cl)

if a_mem > b_mem and a_mem > c_mem :
    print('A')
elif b_mem > a_mem and b_mem > c_mem:
    print('B')
else:
    print('C')

