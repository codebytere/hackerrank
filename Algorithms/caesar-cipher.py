'''
Problem Statement
Julius Caesar protected his confidential information from his enemies by encrypting it. Caesar rotated every letter in the string by a fixed number K. This made the string unreadable by the enemy. You are given a string S and the number K. Encrypt the string and print the encrypted string.
For example:
If the string is middle-Outz and K=2, the encoded string is okffng-Qwvb. Note that only the letters are encrypted while symbols like - are untouched.
'm' becomes 'o' when letters are rotated twice,
'i' becomes 'k',
'-' remains the same because only letters are encoded,
'z' becomes 'b' when rotated twice.

Input Format
Input consists of an integer N equal to the length of the string, followed by the string S and an integer K.
'''

import string
import re

def caesar_cipher():
	result = []

	num_letters = int(raw_input())
	init_str = raw_input()

	shift = int(raw_input())

	shift_low=string.lowercase[shift:]+string.lowercase[:shift]
	shift_up=string.uppercase[shift:]+string.uppercase[:shift]

	for letter in init_str:
		if re.match("\w", letter):
			if letter.isupper():
				result.append(shift_up[string.uppercase.index(letter)])
			elif letter.islower():
				result.append(shift_low[string.lowercase.index(letter)])
		else:
			result.append(letter)
	print "".join(result)

caesar_cipher()
