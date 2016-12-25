from itertools import *

def rot_right(l,n):
  return l[-n:] + l[:-n]

def rot_left(l,n):
  return l[n:] + l[:n]

def f(p):
  f = open('d21.txt')
  l = list(p)
  for line in f:
    sp = line.split()
    digs = [int(x) for x in sp if x.isdigit()]
    if line.startswith('swap position'):
      x,y = digs
      l[x],l[y] = l[y],l[x]
    elif line.startswith('swap letter'):
      x,y = sp[2],sp[-1]
      i,j = l.index(x), l.index(y)
      l[i],l[j] = l[j],l[i]
    elif line.startswith('rotate left'):
      x = digs[0]
      l = rot_left(l,x)
    elif line.startswith('rotate right'):
      x = digs[0]
      l = rot_right(l,x)
    elif line.startswith('rotate based'):
      c = sp[-1]
      i = l.index(c)
      i += (i>=4) + 1
      l = rot_right(l,i%len(l))
    elif line.startswith('reverse'):
      x,y = digs
      l[x:y+1] = l[x:y+1][::-1]
    else:
      x,y = digs
      a = l.pop(x)
      l = l[:y]+[a]+l[y:]
  return ''.join(l)

def f_inv(target):
  for p in permutations(target):
    if f(p)==target:
      return ''.join(p)

print (f_inv('fbgdceah'))