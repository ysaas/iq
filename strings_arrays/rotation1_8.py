#is s2 a rotation of s1
#not working code

def is_rotation(s1, s2):
  
  if s1 == s2:
    return True
    
  if len(s1) != len(s2):
    return False
    
  s1s1 = s1+s1
  
  return isSubstring(s1s1, s2)
  
  