'''
Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.But, to lock the door he needs a key that is an anagram of a certain palindrome string.

The king has a string composed of lowercase English letters. Help him figure out whether any anagram of the string can be a palindrome or not.

Input Format
A single line which contains the input string.
'''

from collections import Counter

def got():
	word = input()
	found = 0
	letter_counts = Counter(word).values()
	odd_counts = [count for count in letter_counts if count % 2 != 0]
	print("YES") if len(odd_counts) <= 1 else print("NO")

got()
