'''
Given an unsorted list of integers, output the integers in order.

Hint: You can use your previous code that counted the items to print out the actual values in order.
'''

def sort_arr():
  num_vals = int(input())
  arr = input().split(" ")
  counts = [0] * (num_vals + 1)
  for num in arr:
    print(num)
    counts[int(num)] += 1

  index = 0;
  for i in range(len(counts)):
    while 0 < counts[i]:
      arr[index] = i
      index += 1
      counts[i] -= 1
  print(" ".join([str(i) for i in arr]))

sort_arr()
