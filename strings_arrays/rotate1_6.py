# given nxn matrix, rotate it 90 degrees
# transpose then reverse

image = [['A','B','C','D'],['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'],['M', 'N', 'O','P']]

def rotate(img):

  n = len(img[0])

  if n==1:
    return img

  new_img = []

  for i in range(n):
    new_img.append([None]*n)
    
  for r in range(n):
    for c in range(n):
      new_img[r][c] = img[c][r]    
  
  for i in range(n):
    new_img[i] = new_img[i][::-1]
      
  return new_img
  
print rotate(image)
      