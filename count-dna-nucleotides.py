#!/usr/bin/env python

f = open('rosalind_dna.txt')
s = f.readline()
print s.count('A'), s.count('C'), s.count('G'), s.count('T')
f.close()
