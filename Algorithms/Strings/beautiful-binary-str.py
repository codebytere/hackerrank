'''
Alice has a binary string, , of length . She thinks a binary string is beautiful if and only if it doesn't contain the substring .

In one step, Alice can change a 0 to a 1 (or vice-versa). Count and print the minimum number of steps needed to make Alice see the string as beautiful.
'''

def flip(tfl, ind):
  tfl = list(tfl)
  tfl[ind] = '0' if tfl[ind] == '1' else '1'
  return ''.join(tfl)

def make_beautiful():
  str_len = int(input())
  bin_str = input()
  count = 0

  while '010' in bin_str:
    count += 1
    flip_ind = bin_str.find('010') + 2
    bin_str = flip(bin_str, flip_ind)

  print(count)

make_beautiful()
