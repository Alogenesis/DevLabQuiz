'''
ทำการหาผลรวมของตัวเลขทุกตัวที่นำมาบวกกัน
'''

num_input = input()



now_len = len(num_input)
print(now_len)

while now_len > 1 :
    #Append string to lib
    num_lib = []
    for i in num_input:
        num_lib.append(i)
    print(num_lib)

    # Change str to int and SUM!!
    sum = 0
    for i in num_lib:
        sum += int(i)
    # Check answer
    print(sum)
    num_input =  str(sum)

    #Clear num_lib
    now_len = len(num_input)
    print(now_len)
    num_lib = []

print(num_input)









