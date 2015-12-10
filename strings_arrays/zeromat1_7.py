# Write an algorithm s. t. if an element in an MxN matrix is 0, 
# its entire row and column are set to 0

import numpy as np

mat = [[1,2,0,0],[1,3,4,6],[1,2,3,4],[0,3,4,5]]

def zeroize(mat):
  
  m = len(mat)
  n = len(mat[0])
  
  if (m==1) and (n==1):
    return mat
    
  new_mat = np.zeros((m,n), dtype=np.int) 
  
  zero_cols = set()
  zero_rows = set()
  
  #find the index of zeros 
  for r in range(m):
    for c in range(n):
      if mat[r][c] == 0:
        zero_cols.add(c)
        zero_rows.add(r)
  
  #copy over those numbers not in zero rows or cols
  for r in range(m):
    if r not in zero_rows:
      for c in range(n):
        if c not in zero_cols:
          new_mat[r][c] = mat[r][c]
        
  return new_mat
  
print zeroize(mat)