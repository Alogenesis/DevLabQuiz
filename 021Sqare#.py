'''
In : 5
Out :
#####
#   #
#   #
#   #
#####
'''

n = int(input('Type a number : '))

if n == 1 :
	print('#'*n)
else :
	print('#'*n)
	for i in range(n-2):
		print('#' + (' '*(n-2)) + '#')
	print('#'*n)