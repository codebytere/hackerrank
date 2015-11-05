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
<<<<<<< HEAD
=======
import re
>>>>>>> e860304519c5d97b38cadfd1213ad3c04f81dedd

def caesar_cipher():
	result = []

	num_letters = int(raw_input())
	init_str = raw_input()

	shift = int(raw_input())
	l_shift = shift%26

	shift_low=string.lowercase[l_shift:]+string.lowercase[:l_shift]
	shift_up=string.uppercase[l_shift:]+string.uppercase[:l_shift]
	shift_num= map(int, range(0, 10))[shift%9:]+map(int, range(0, 10))[:shift%9]

	for symbol in init_str:
		if symbol.isalpha():
			if symbol.isupper():
				result.append(shift_up[string.uppercase.index(symbol)])
			elif symbol.islower():
				result.append(shift_low[string.lowercase.index(symbol)])
		elif symbol.isdigit():
			result.append(str(shift_num[(int(symbol))]))
		else:
			result.append(symbol)
caesar_cipher()
