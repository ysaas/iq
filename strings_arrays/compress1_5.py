# Does basic string compression.  If compression doesn't produce shorter 
# string, return original string

# python compress1_5.py aabcccccaaa
# output: a2b1c5a3

# python compress1_5.py aaabbccdaa
# output: aaabbccdaa
import sys

string = sys.argv[1]

def compress(s):
  if(len(s) == 1):
    return s
  
  cstring = ''
  
  current_letter = s[0]
  current_count = 1
  
  for c in s[1:]:  
    if(c == current_letter):
      current_count += 1
    else:
      cstring += current_letter + str(current_count)
      current_letter = c
      current_count = 1
  
  cstring += current_letter + str(current_count)
  
  if (len(cstring) >= len(s)):
    return s
  else:
    return cstring
    
print compress(string)