'''
Output
    $
   $ $
  $ $ $
 $ $ $ $
$ $ $ $ $
'''

backspace = 4
sign = '$ '
sign_end = '$'
for i in range(5):
  print( (' ' * backspace)+(sign * i)+(sign_end) )
  backspace = backspace - 1