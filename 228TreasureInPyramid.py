'''
5
    #
   ###
  ##♦##
 #######
#########
'''

x = int(input())

space = x - 1
dot = 1
lst = []
mid_lst = ((x + 1) /2) - 1

for i in range(0,x):
    if i != int(mid_lst):
        txt = ' '*space + '#'*dot
        space -= 1
        dot += 2
        lst.append(txt)
    else:
        txt = ' ' * space + '#' * int((dot-1)/2) + '♦' +'#' * int((dot-1)/2)
        space -= 1
        dot += 2
        lst.append(txt)

print(lst)


#Change midlist
lst[int(mid_lst)]

for i in lst:
    print(i)

