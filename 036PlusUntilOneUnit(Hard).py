'''
ให้ทำการบวกตัวเลขทุกจากจำนวนเต็มที่รับเข้ามา หาผลรวมของตัวเลขทุกตัวมากกว่า 1 หลัก ให้ทำซ้ำไปเรื่อยๆจนเหลือเลข 1 ตัว
Input:
67896789678967896879678967896789678967896789678969
Output:6
'''

x = input('Number : ')
lenx = len(x)
#print('len x =', lenx)
#print('max index =', lenx-1)
#print(lenx)
result = 0
n_index = 0

print('Get', x , type(x))
result = int(x[n_index])
#print('start =',result)
#Sum All of string
result_int = 2

while result_int > 1 :

    while n_index != lenx-1:
        #print(result ,"+", x[n_index +1])
        result += int(x[n_index +1])
        n_index += 1
        #print('Result =', result)
        #print('Index =', n_index)
        #print(int(x[n_index]) + int(x[n_index +1]))
        print('=',result)   #Answer
        #print('Now index start =',n_index)
    result_str = str(result)
    print('len_str =',len(result_str))
    result_int = int(result_str)
    print('Now Result_int class =', type(result_int))
    n_index = 0
    print('Now n index = ', n_index)
    lenx = len(result_str)
    print('Now lenx =', lenx)
    x = result_str
    print('now x =', x , 'class =', type(x))
    result = int(x[0])
    if len(x) > 1 :
        continue
    else:
        break

print('--------')
print(result)
print('--------')