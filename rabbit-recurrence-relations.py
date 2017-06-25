#!/usr/bin/env python

# T(n) = T(n-1) + 3T(n-2)
# 1 1 4 7 19
# Recursive Fibonacci
def fib_rabbits(n, k):
   if (n == 1 or n == 2):
      return 1
   else:
      return fib_rabbits(n-1, k) + 3*(fib_rabbits(n-2, k))

if __name__ == '__main__':
#   f = open('rosalind_rabbits.txt', 'r')
#   s = f.readline()
#   f.close()
   #n, k = s.split(' ')

   n = 5
   k = 3
   print fib_rabbits(n, k)

# Dynamic Programming Fibonacci
