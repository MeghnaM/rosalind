#!/usr/bin/env python

#f = open('rosalind_gc.txt','r')
#s = f.readline()
#f.close()

def gc_content(dna):
   gc_total = float(dna.count('G') + dna.count('C'))
   dna_total = gc_total + float(dna.count('A') + dna.count('T'))
   return (gc_total/dna_total) * 100

def parseFileContentsAndCalculateGCmax(string):
   string_id = ''
   dna = ''
   for x in string:
      if x == '>':
         string_id = string_id + x

if __name__ == '__main__':
   gc_max = 0
   str_id = ''
   dna = ''

   # TODO Read lines from file, calculate GC content for all dna strings,
   # then print the id of the one which won, and its GC content in the next line
   with open('rosalind_gc_test.txt','r') as f:
      while True:
         line = f.readline()
         if line and (line[0] == '>'):
            str_id = line
            print "str_id", str_id
         line2 = f.readline()
         if not line2: break
         #if line2[0] != '<':
         dna = dna + line2.strip()
         #elif line2[0] == '<': break
         #gc_max = gc_content(dna)
      print "dna", dna

   print gc_max
   # TODO Experiment: Try to write this output to a file
   #dna = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
   # TODO Truncate floating point number to be 6 decimal places (without rounding)
   #print gc_content(dna)

