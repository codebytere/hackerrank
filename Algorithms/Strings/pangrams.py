'''
Problem Statement
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)
After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.
Given a sentence s, tell Roy if it is a pangram or not.

Input Format
Input consists of a line containing s.
'''

def pangrams():
    in_str = raw_input()
    if not set('abcdefghijklmnopqrstuvwxyz') - set(in_str.lower()):
        print "pangram"
    else:
        print "not pangram"

pangrams()