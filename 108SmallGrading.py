'''
0-25 = fail
26-50 = good
51-75 = very good
76-100 = excellent

In : 20
Out : fail
'''

x = int(input())
if x >= 76:
    print('excellent')
elif x > 51:
    print('very good')
elif x > 26:
    print('good')
else:
    print('fail')