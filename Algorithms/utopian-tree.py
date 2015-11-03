'''
Problem Statement
The Utopian Tree goes through 2 cycles of growth every year. The first growth cycle occurs during the spring, when it doubles in height. The second growth cycle occurs during the summer, when its height increases by 1 meter. Now, a new Utopian Tree sapling is planted at the onset of spring. Its height is 1 meter. Can you find the height of the tree after N growth cycles?

Input Format
The first line contains an integer, T, the number of test cases.
T lines follow; each line contains an integer, N, that denotes the number of cycles for that test case.
'''

import sys

def utopian_tree():
  cycles = []
  numCycles = int(raw_input())

  for i in range(0, numCycles):
    cycles.append(int(raw_input()))

  for cycle in cycles:
    treeHeight = getHeight(cycle)
    print treeHeight

def getHeight(numCycles):
  height = 1
  for i in range(0, numCycles):
    if(i%2 == 0):
      height*=2
    else:
      height+=1
  return height

utopian_tree()
