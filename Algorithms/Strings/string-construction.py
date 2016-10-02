'''
Amanda has a string, s , of m lowercase letters that she wants to copy into a new string, . She can perform the following operations any number of times to construct string :

1) Append a character to the end of string p at a cost of  dollar.
2) Choose any substring of p and append it to the end of p at no charge.

Given  strings, find and print the minimum cost of copying each s_1 to p_1 on a new line.
'''

def main():
  num_cases = int(input())
  ret = []
  for case in range(num_cases):
    s_t_m = input()
    ret.append(construct_string(s_t_m))

  print("\n".join(ret))

def power_set(string):
  p_s = []
  if len(string) == 0:
      p_s.append("")
      return p_s
  first = string[0]
  rem = string[1:len(string)]
  words = power_set(rem)
  p_s.extend(words)
  for word in words:
      p_s.append(first+word)
  return p_s

def construct_string(word):
  price = 1;
  con_str = word[0]

  pow_set = power_set(word)
  print(pow_set)

  while(con_str != word):
    print(con_str)
    if (con_str in word) and (word.count(con_str) > 1):
      con_str += con_str
    else:
      ind = len(con_str)
      con_str += word[ind]
      price += 1

  return price

main()
