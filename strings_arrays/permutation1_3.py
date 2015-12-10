#Given two stirngs, write a method to decide if one is a permutation of the other.
# run: python permutation1_3.py 'abcde' 'acbde'
# output: True

# run: python permutation1_3.py 'abcde' 'acfbde'
# output: False

import sys

string1 = sys.argv[1]
string2 = sys.argv[2]

def is_permutation(s1, s2):
  if len(s1)!=len(s2):
    return False
  
  if sorted(s1) == sorted(s2):
    return True
  else:
    return False

print is_permutation(string1, string2)    
