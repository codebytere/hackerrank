'''
In the Quicksort challenges, you sorted an entire array. Sometimes, you just need specific information about a list of numbers, and doing a full sort would be unnecessary. Can you figure out a way to use your partition code to find the median in an array?

Challenge
Given a list of numbers, can you find the median?
'''

def find_median():
  arr_len = int(input())
  arr = input().split(" ")
  ret = sorted([int(num) for num in arr])
  print(ret[(arr_len//2)])

find_median()
