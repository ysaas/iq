# string.replace(' ', '%20')
# Write a method to replace all spaces in a string with '%20'...do in place...

# run: python replace1_4.py 'Mr John Smith' 
# output: Mr%20John%20Smith
import sys

string = sys.argv[1]
length = int(sys.argv[2])

def replace_with(string, length):
  string_list = list(string)
  new_length = length
  
  for i in range(length):
    if string_list[i] == ' ':
      string_list[i] = '%20'
      new_length += 2
  return ''.join(string_list)[:new_length]

print replace_with(string, length)