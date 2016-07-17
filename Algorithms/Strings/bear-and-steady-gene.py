from collections import Counter

def bear_steady_gene():
  len_gene = int(input())
  gene = input()
  gene_ctr = Counter(gene)
  
  if is_steady(gene, gene_ctr):
    print(0)
  else:
    result = float("inf")
    out = 0
    for num in range(len_gene):
      gene_ctr[gene[num]] -= 1
      while is_steady(gene, gene_ctr) and out <= num:
          result = min(result, num - out + 1)
          gene_ctr[gene[out]] += 1
          out += 1

    print(result)

def is_steady(gene, gene_ctr):
  return True if all(t <= len(gene)/4 for t in gene_ctr.values()) else False

bear_steady_gene()