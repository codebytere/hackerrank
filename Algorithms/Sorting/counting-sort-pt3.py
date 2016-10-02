'''
You will be given a list that contains both integers and strings. In this challenge you just care about the integers. For every value  from , can you output , the number of elements that are less than or equal to ?
'''

def sort_arr():
  num_vals = int(input())
  arr = []
  sorts = [0] * (100)
  for obj in range(num_vals):
    arr.append(int(input().split(" ")[0]))

  for num in range(100):
    sorts[num] = len([x for x in arr if x <= num])

  print(" ".join([str(i) for i in sorts]))

sort_arr()
