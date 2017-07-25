#!/usr/bin/env python

# Hamming distance - The minimum number of symbol substitutions required to change one string into another of equal length
def count_pt_mutations(s,t):
   if (len(s) != len(t)): return -1
   hdist = 0
   los = list(s)
   lot = list(t)
   for i in range(len(los)):
      if los[i] != lot[i]: hdist += 1
   return hdist

if __name__ == '__main__':
   f = open('rosalind_hamm.txt','r')
   s = f.readline()
   t = f.readline()
   print count_pt_mutations(s,t)
