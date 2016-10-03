'''
Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w. In case of multiple possible answers, find the lexicographically smallest one among them.

Input Format
The first line of input contains t, the number of test cases. Each of the next t lines contains w.
'''

def main():
  num_strs = int(input())
  ret =[]
  for word in range(num_strs):
    word = input()
    ret.append(get_next_greater(word))

  print("\n".join(ret))

def get_next_greater(word):
  word = list(word)
  idx1 = len(word) - 1
  while idx1 > 0 and word[idx1 - 1] >= word[idx1]:
      idx1 -= 1
  if idx1 <= 0:
      return "no answer"

  idx2 = len(word) - 1
  while word[idx2] <= word[idx1 - 1]:
      idx2 -= 1

  word[idx1 - 1] = word[idx2]
  word[idx2] = word[idx1 - 1]

  word[idx1:] = word[len(word)-1:idx1-1:-1]
  return "".join(word)

main()
