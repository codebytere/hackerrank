'''
Problem Statement
Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format
The first line contains an integer T, i.e. the number of test cases. 
The next T lines contain a string each.
'''

def alternating_chars():
    num_cases = int(raw_input())
    results = []
    for case in range(num_cases):
        line = raw_input()
        prev, changes  = line[0], 0
        for char in line[1:]:
            if prev == char:
                changes += 1
            prev = char
        results.append(str(changes))
    print "\n".join(results)

alternating_chars()