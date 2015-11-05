from math import ceil,sqrt

def encryption():
	result = []
	sentence = raw_input().replace(" ", "")
	cols = int(ceil(sqrt(len(sentence))))
	for col in range(cols):
		result.append(sentence[col::cols])
	print " ".join(result)

encryption()
