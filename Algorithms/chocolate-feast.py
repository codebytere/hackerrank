'''
Problem Statement

Little Bob loves chocolate, and he goes to a store with $N in his pocket. The price of each chocolate is $C. The store offers a discount: for every M wrappers he gives to the store, he gets one chocolate for free. How many chocolates does Bob get to eat?

Input Format:
The first line contains the number of test cases, T.
T lines follow, each of which contains three integers, N, C, and M.
'''

def feast():
	T = int(input())
	for i in range(T):
			money, choc_price, wrap_min = map(int,input().split())
			total = wrappers = money
			while wrappers >= wrap_min:
					total += wrappers
					wrappers = (wrappers % wrap_min) + (wrappers // wrap_min)
			print(total)

feast()
