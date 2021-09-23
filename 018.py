'''Pyramid
In : 5
Out :
    *
   ***
  *****
 *******
*********
'''

get = int(input('Type a number : '))
dot = '*'
space = ' '
space_multiply = get - 1
dot_end = '**'
for i in range(get):
    print((space * space_multiply) + (dot * (2 * (i + 1) - 1)))
    space_multiply = space_multiply - 1

    # 2x - 1