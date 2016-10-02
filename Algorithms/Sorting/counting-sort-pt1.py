'''
Challenge
Given a list of integers, can you count and output the number of times each value appears?

Hint: There is no need to sort the data, you just need to count it.
'''

def count_appearances():
  ret = ""
  num_vals = int(input())
  arr = input().split(" ")
  for num in range(100):
    ret += str(arr.count(str(num))) + " "
  print(ret)

count_appearances()
