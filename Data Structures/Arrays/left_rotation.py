'''
A left rotation operation on an array of size  shifts each of the array's elements  unit to the left. For example, if left rotations are performed on array , then the array would become .

Given an array of  integers and a number, , perform  left rotations on the array. Then print the updated array as a single line of space-separated integers.

Input Format

The first line contains two space-separated integers denoting the respective values of  (the number of integers) and  (the number of left rotations you must perform).
The second line contains  space-separated integers describing the respective elements of the array's initial state.
'''

def left_rotate():
  params = input().split(" ")
  num_ints, num_rotations = int(params[0]), int(params[1])
  arr = input().split(" ")

  ret = ""
  for index in range(num_rotations + 1):
    ret += arr[(index+num_rotations) % num_ints] + " "
  print(ret)

left_rotate()

