'''
input : 12345 (second)
Out : 3:25:45
'''

x = int(input())
sec = 0
min = 0
hour = 0

while x > 0:
    if x >= 3600:
        x = x - 3600
        hour += 1
    elif x >= 60:
        x = x - 60
        min += 1
    elif x > 0:
        sec = x
        x -= x

print('{}:{:02d}:{:02d}'.format(hour,min,sec))

