'''
There are two kangaroos on an x-axis ready to jump in the positive direction (i.e, toward positive infinity). The first kangaroo starts at location  and moves at a rate of  meters per jump. The second kangaroo starts at location  and moves at a rate of  meters per jump. Given the starting locations and movement rates for each kangaroo, can you determine if they'll ever land at the same location at the same time?
'''

def kangaroo():
  (x1, v1, x2, v2) = [int(x) for x in input().split()]
  print(do_they_cross(x1, v1, x2, v2))

def do_they_cross(x1, v1, x2, v2):
  if x2 > x1 and v2 > v1:
    return("NO")
  elif x1 != x2 and v1 == v2:
    return("NO")
  if x1 == x2:
    return("YES")
  elif x1 < x2:
    while x1 <= x2:
        if x1 == x2:
          return("YES")
        x1 = x1 + v1
        x2 = x2 + v2
  else:
    while x2 <= x1:
        if x1 == x2:
          return("YES")
        x1=x1+v1
        x2=x2+v2
  return("NO")

kangaroo()
