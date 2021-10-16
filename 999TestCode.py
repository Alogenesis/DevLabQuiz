user_input = input()
spl1, spl2 = user_input.split(' ')
last = int(spl1)
loop_get = int(spl2)

way = []
for i in range(0,loop_get) :
    x = input()
    way.append(x)
#print(way)

time = 0
#find last
target = last
way_lst = []
while target != 1 :
    for i in way:
        way_temp = []
        y = i.split(' ')
        way_lst.append(y)   #add for print
        way_temp.append(y)  #add for split
        a11,a22,a33 = i.split(' ')
        a1 = int(a11)
        a2 = int(a22)
        a3 = int(a33)
        if a2 == target :
            #print('>>> target =',a2)
            time += a3
            target = a1
            break
        else:
          pass
            #print(way)('not target')

        #print(way)('now target =',target)
        #print(way)('time =',time)

#print(way)('last target =',target)
print(time)
