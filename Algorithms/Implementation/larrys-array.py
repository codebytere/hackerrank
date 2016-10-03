'''
Larry has a permutation of  numbers whose unique elements range from 1 to N. He wants  to be sorted, so he delegates the task of doing so to his robot. The robot can perform the following operation as many times as it wants:

Choose any  consecutive indices and rotate their elements in such a way that (1,2,3) rotates to (2,3,1), which rotates to (3,1,2), which rotates back to (1,2,3).

On a new line for each test case, print YES if the robot can fully sort; otherwise, print NO.
'''

def larrys_array():
  num_cases = int(input())
  ret = []
  for case in range(num_cases):
    arr_len = int(input())
    arr = [int(x) for x in input().split(" ")]
    num_inversions = 0
    for i in range(0, arr_len):
      for j in range (i+1, arr_len):
        if arr[i] > arr[j]:
          num_inversions += 1
    print(num_inversions)

    ret.append("YES") if (num_inversions % 2 == 0) else ret.append("NO")

  print("\n".join(ret))

larrys_array()
