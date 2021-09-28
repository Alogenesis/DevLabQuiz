'''
1. เลือก เฉพาะ input ที่นำหน้าด้วย GUITAR:
2. ลบเครื่องหมายพิเศษบน string ที่ได้มา
3. แสดงกลับไป
In :
SO_GOD:[Buffe, loger, pitch]
Nobacj:[sorener, fetch_assoc]
GUITAR:[dam, !@D@H, (*!@^, #@%(^]

Out :
GUITAR:[dam]
'''

x = input()
y = input()
z = input()
#print(x[0])
#print(y[0])
#print(z[0])

select = 0

if x[0] == 'G':
    select = x
elif y[0] == 'G':
    select = y
else:
    select = z

#print(select)
re_select1 = select.replace('GUITAR:[','')
re_select2 = re_select1.replace(']','')
re_select = re_select2.split(', ')
#print('reselect =',re_select)
#print(len(re_select))
first = 'GUITAR:['
mid = []
last = ']'

spc = '!@#$%^&*()_'
miss = 0
n = 0

while n != len(re_select):
    for i in spc: #2nd run
        for j in re_select[n]: #1st run
            #print(j, 'and', i) #test code
            #print('type j =',type(j),'and type i =',type(i))
            if i == j:
                miss = miss + 1
            else:
                pass
    print(miss)
    if miss == 0 :
        mid.append(re_select[n])
    else:
        pass
    miss = 0
    n = n + 1

print(mid)
print(n)


print(first,end='')
print(*mid,sep=', ',end='')
print(last)
