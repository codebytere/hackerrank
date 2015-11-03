'''
Problem Statement
Sherlock Holmes is getting paranoid about Professor Moriarty, his arch-enemy. All his efforts to subdue Moriarty have been in vain. These days Sherlock is working on a problem with Dr. Watson. Watson mentioned that the CIA has been facing weird problems with their supercomputer, 'The Beast', recently. This afternoon, Sherlock received a note from Moriarty, saying that he has infected 'The Beast' with a virus. Moreover, the note had the number N printed on it. After doing some calculations, Sherlock figured out that the key to remove the virus is the largest Decent Number having N digits.A Decent Number has the following properties:
3, 5, or both as its digits. No other digit is allowed.
Number of times 3 appears is divisible by 5.
Number of times 5 appears is divisible by 3.
Meanwhile, the counter to the destruction of 'The Beast' is running very fast. Can you save 'The Beast', and find the key before Sherlock?

Input Format
The 1st line will contain an integer T, the number of test cases. This is followed by T lines, each containing an integer N. i.e. the number of digits in the number.
'''

def save_the_beast():
	decents = []
	num_cases = int(raw_input())
	for case in range(num_cases):
		n = int(raw_input())
		rem = n % 3
		threes = ((3 - rem) % 3) * 5
		fives = n - threes
		if fives < 0:
				decents.append(-1)
		else:
				decents.append(int("5"*fives + "3"*threes))

	for decent in decents:
		print decent

save_the_beast()

