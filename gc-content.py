#!/usr/bin/env python

#f = open('rosalind_gc.txt','r')
#s = f.readline()
#f.close()

def gc_content(dna):
   gc_total = float(dna.count('G') + dna.count('C'))
   dna_total = gc_total + float(dna.count('A') + dna.count('T'))
   return (gc_total/dna_total) * 100

if __name__ == '__main__':
   # TODO Read lines from file, calculate GC content for all dna strings,
   #      then print the id of the one which won, and its GC content in the next line
   # TODO Experiment: Try to write this output to a file
   dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
   # TODO Truncate floating point number to be 6 decimal places (without rounding)
   print gc_content(dna)

