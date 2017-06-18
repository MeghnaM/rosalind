#!/usr/bin/env python

f = open('rosalind_revc.txt','r')
s = f.readline() # Reads one entire line from the file and stores it as a string, along w/ a trailing newline char
f.close()

def complement(s):
   st = ''
   for i in s:
      if (i == 'A'):
         st += 'T'
      elif (i == 'T'):
         st += 'A'
      elif (i == 'G'):
         st += 'C'
      elif (i == 'C'):
         st += 'G'
   print st

complement(s[::-1]) # [start, stop, step]
