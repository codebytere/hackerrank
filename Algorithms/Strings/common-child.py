'''
Given two strings a and b of equal length, what's the longest string (S) that can be constructed such that it is a child of both?

A string x is said to be a child of a string y if x can be formed by deleting 0 or more characters from y.

For example, ABCD and ABDC has two children with maximum length 3, ABC and ABD. Note that we will not consider ABCD as a common child because C doesn't occur before D in the second string.

Input format
Two strings,  and , with a newline separating them.
'''

def common_child():
  str_one = input()
  str_two = input()
  lengths = [[0 for j in range(len(str_two)+1)] for i in range(len(str_one)+1)]
  for i, x in enumerate(str_one):
    for j, y in enumerate(str_two):
      if x == y:
        lengths[i+1][j+1] = lengths[i][j] + 1
      else:
        lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

  print(lengths[-1][-1])

common_child()

OUDFRMYMAW
AWHYFCCMQX
