'''
Problem Statement
Sid is obsessed with reading short stories. Being a CS student, he is doing some interesting frequency analysis with the books.

Your task is to help him find the minimum number of characters of the first string he needs to change to enable him to make it an anagram of the second string.

Note: A word x is an anagram of another word y if we can produce y by rearranging the letters of x.

Input Format
The first line will contain an integer, T, representing the number of test cases. Each test case will contain a string having length len(S1)+len(S2), which will be concatenation of both the strings described above in the problem.The given string will contain only characters from a to z.
'''

def anagram():
    num_strings = int(raw_input())
    result = []
    for i in range(num_strings):
        string = raw_input()
        if len(string)%2 != 0:
            result.append(str(-1))
        else:
            p1,p2 = string[:len(string)/2], string[len(string)/2:]
            if sorted(p1) == sorted(p2):
                result.append(str(0))
            else:
                diff = len([x for x in list(p1) if x not in list(p2)])
                result.append(str(diff))
    print "\n".join(result)

anagram()