#!/usr/bin/env python3

top = '\u2581' #u23af
left = '\u2595'
right = '\u258e'
bottom = '\u2594'

l = 100
h = l * 2

print(' ' + top * h + ' ')

i = 0
while i < l:
    print(left + '\033[41m ' * h + '\033[0m' + right)
    i += 1
print(' ' + bottom * h + '\033[0m ')
