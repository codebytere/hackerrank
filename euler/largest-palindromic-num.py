'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest(bottom, top):
  largest = 0
  for first in range(top, bottom, -1):
    for second in range(top, bottom, -1):
      if is_palindrome(first*second):
        if first*second > largest:
          largest = first*second
  return largest

print(largest(100,999))
