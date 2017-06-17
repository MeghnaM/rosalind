#!/usr/bin/env python

f = open('rosalind_rna.txt','r')
s = f.readline()
print s.replace('T','U')
f.close()
