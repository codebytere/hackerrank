'''
Challenge
In the previous challenge, you created a "helper array" that contains information about the starting position of each element in a sorted array. Can you use this array to help you create a sorted array of the original list?

Hint: You can go through the original array to access the strings. You can then use your helper array to help determine where to place those strings in the sorted array. Be careful about being one off.

Details and a Twist
You will be given a list that contains both integers and strings. Can you print the strings in order of their accompanying integers? If the integers for two strings are equal, ensure that they are print in the order they appeared in the original list.

The Twist - Your clients just called with an update. They don't want you to print the first half of the original array. Instead, they want you to print a dash for any element from the first half.

Input Format
n, the size of the list ar.
n  lines follow, each containing an integer x and a string s.
'''

def sort_arr():
  items = []
  num_items = int(input())

  for position in range(num_items):
    item = input().split(" ")
    items.append((int(item[0]), item[1], position,))

  sorted_arr = sorted(items, key=lambda element: element[0])

  ret = ""
  for elem in sorted_arr:
    if elem[2] >= num_items/2:
      ret += elem[1] + " "
    else:
      ret += "- "

  print(ret)
sort_arr()

'''
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

- - - - - to be or not to be - that is the question - - - -
'''
