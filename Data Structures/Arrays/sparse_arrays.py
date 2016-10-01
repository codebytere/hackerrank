'''
There are  strings. Each string's length is no more than  characters. There are also  queries. For each query, you are given a string, and you need to find out how many times this string occurred previously.

Input Format

The first line contains , the number of strings.
The next N lines each contain a string.
The N + 2nd line contains Q, the number of queries.
The following Q lines each contain a query string.
'''

def main():
  num_strings = int(input())
  strings = []
  for s in range(num_strings):
    strings.append(input())

  ret = []
  num_queries = int(input())
  for q in range(num_queries):
    query = input()
    ret.append(str(strings.count(query)))
  print("\n".join(ret))

main()
