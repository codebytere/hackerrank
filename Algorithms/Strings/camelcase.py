'''
Alice wrote a sequence of words in CamelCase as a string of letters, , having the following properties:

It is a concatenation of one or more words consisting of English letters.
All letters in the first word are lowercase.
For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
Given i, print the number of words in  on a new line.
'''

def camel_case():
  cc_str = input()
  num_uppers = len([ch for ch in cc_str if ch.isupper()])
  print(num_uppers + 1)

camel_case()
