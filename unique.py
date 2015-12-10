#Question 1.1
# Implement an algorithm to determine if a string has all unique characters. 
# what if you cannot use additional data structure
# Note: doesn't check spaces

import sys

string = sys.argv[1]
print string

def check_unique(string):
  for i in range(len(string)-1):
    if string[i] in string[i+1:]:
      return(False)
    else:
      return(True)

print check_unique(string)
