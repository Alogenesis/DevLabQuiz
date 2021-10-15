num_input = input()
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
