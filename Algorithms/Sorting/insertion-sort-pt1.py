'''
Problem Statement

Insert element into sorted list 
Given a sorted list with an unsorted number  in the rightmost cell, can you write some simple code to insert  into the array so that it remains sorted?

Print the array every time a value is shifted in the array until the array is fully sorted. The goal of this challenge is to follow the correct order of insertion sort.

Guideline: You can copy the value of  to a variable and consider its cell "empty". Since this leaves an extra cell empty on the right, you can shift everything over until  can be inserted. This will create a duplicate of each value, but when you reach the right spot, you can replace it with .

Input Format

There will be two lines of input:
1. the size of the array
2. the unsorted array of integers
'''

def insertion_sort():
  arr_sz = int(input())
  arr = [int(x) for x in input().split()]
  
  least = arr[arr_sz - 1]
  is_sorted = False
  
  for i in range(arr_sz - 1, 0, -1):
    if arr[i - 1] > least:
        arr[i] = arr[i - 1]
        print(" ".join(map(str, arr)))
    else:
      arr[i] = least
      is_sorted = True
      break
  if not is_sorted:
    arr[0] = least
  print(" ".join(map(str, arr)))

insertion_sort()