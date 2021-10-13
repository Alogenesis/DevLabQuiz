import math

#input
member_input = int(input())
n_lib = []
for i in range(0,member_input):
    n = int(input())
    n_lib.append(n)

print(n_lib)


# Run time
an = [0]
result = 0

for i in range(1,15):
    result = math.sqrt(1 + (an[-1]**2))
    an.append(result)

print(an)

order = []
sum_order = 0
for i in range(1,14):
    result = 1 / (an[i]+an[i+1])
    sum_order += result
    order.append(sum_order)
    print(sum_order)
print(order)



for i in range(0,member_input):
    sum_result = order[n_lib[i] -2]
    print('{:.2f}'.format(sum_result))