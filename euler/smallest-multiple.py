'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from functools import reduce


def prime_factors(n):
  factors = []
  d = 2
  while n > 1:
    while n % d == 0:
      if(n != d):
        factors.append(d)
      n /= d
    d += 1
  return factors

def smallest_multiple():
  factors = []
  for num in range(1,21):
    if len(prime_factors(num)) == 0:
      factors.append(num)
  return reduce(lambda x,y: x*y, factors)

print(smallest_multiple())
