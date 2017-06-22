#!/usr/bin/env python

# Hamming distance - The minimum number of symbol substitutions required to change one string into another of equal length
def count_pt_mutations(s,t):
   if (len(s) != len(t)): return -1
   dist = 0

   #1 Map over both strings simultaniously, and create a 3rd list of 1's (mismatch) and 0's (match), then reduce the 3rd list by adding all elements

   return result

if __name__ == '__main__':
   s = 'GAGCCTACTAACGGGAT'
   t = 'CATCGTAATGACGGCCT'
   print count_pt_mutations(s,t)
