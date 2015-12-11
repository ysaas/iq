
class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    
    def __str__(self):
      return str(self.data)
      
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
    def set_data(self, new_data):
        self.data = new_data
class LinkList:

  def __init__(self):
    self.head = None
    
  def __str__(self):
    string = ""
    if self.is_empty():
      return string
      
    current = self.head
    string += str(current.get_data())
    while(current.get_next() != None):
      current = current.get_next()
      string += '->'+str(current)
    return string
    
  def is_empty(self):
    return(self.head == None)
    
  def add_front(self, item):
    temp = Node(item, self.head)
    self.head = temp
    
  def add_end(self, item):
    temp = Node(item)

    if self.size() == 0:
      self.head = temp
    else:
      current = self.head
      while(current.get_next() != None):
        current = current.get_next()
      current.set_next(temp)
    
  #2.1 remove all duplicates in place not other stuctures 
  def remove_dup(self):
    current = self.head
    while current != None:
      current_item = current.get_data()
      runner = current
      while runner.get_next() != None:
        if(runner.get_next().get_data() == current_item):
          runner.set_next(runner.get_next().get_next())
        else:
          runner = runner.get_next()
      current = current.get_next()
    
  def size(self):
    current = self.head
    count = 0
    while(current != None):
      count +=1
      current = current.get_next()
    return count
    
  #2.2 find kth to last element
  def kth_last(self, k):
    current = self.head
    s = self.size()
    if (s == k):
      return current.get_data()
      
    k = self.size() - k
    while ((current.get_next() != None) and (k >0)):
      k-=1
      current = current.get_next()
    return current.get_data()
  
# 2.3 delete node given only access to this node in singley linked list
# did not test yet 
  def delete(node):
    node.set_data(node.get_next().get_data())
    node.set_next(node.get_next().get_next())
   
# 2.4 partition around value x
  def part_by(self,x):
    
    if self.size()==0:
      return 
      
    new_list = LinkList()
    current = self.head
    
    while(current != None):
      if current.get_data() >= x:
        new_list.add_end(current.get_data())
      else:
        new_list.add_front(current.get_data())
      print str(new_list)  
      current = current.get_next()
        
      self.head = new_list.head
  
  def get_tail(self):
    if(self.size() <=1):
      return self.head
      
    current = self.head
    while (current.get_next() != None):
      current = current.get_next()  
    return current
    
def reverse(l):
  if l.size()<=1:
    return l
    
  new_list = LinkList()
  current = l.head
  
  while(current != None):
    new_list.add_front(current.get_data())
    current = current.get_next()
  return new_list
  
#2.5 add 2 lists ones digit is at head of list
# input list1 =  9->7->1->6 list2 = 5->9->2
# output 4->7->4->6
def add_lists(l1, l2):
  
  if l1.size() == 0:
    return l2
  if l2.size() == 0:
    return l1
  
  ans = LinkList()
  
  current1 = l1.head
  current2 = l2.head
  carry = 0
  while((current1 != None) or (current2 != None)):
    if current1 == None:
      num1 = 0
      next1 = current1
    else:
      num1 = current1.get_data()
      next1 = current1.get_next()
    if current2 == None:
      num2 = 0
      next2 = current2
    else:
      num2 = current2.get_data()
      next2 = current2.get_next()
      
    sum =  num1 + num2 + carry
    digit1 = sum%10
    ans.add_end(digit1)
    carry = (sum - digit1)/10
    
    current1 = next1
    current2 = next2
  
  
  return ans
    

# 2.7 check if list is a palindrome   
def palindrome(l):
 
  if l.size() <= 1:
    return l
    
  rev_list = reverse(l)
  current = l.head
  rcurrent = rev_list.head
  
  while(current != None):
    if current.get_data() != rcurrent.get_data():
      return False
    current = current.get_next()
    rcurrent = rcurrent.get_next()
  
# l1 = LinkList()
# l2 = LinkList()

# l1.add_front(6) 
# l1.add_front(1) 
# l1.add_front(7)
# l1.add_front (9)

# l2.add_front(2)  
# l2.add_front(9)  
# l2.add_front(5)

# print str(l1)
# print str(l2)  
 
# ans = add_lists(l1, l2)
# print str(reverse(ans)) 
# ll = LinkList()
# ll.add_front('D')
# ll.add_front('B')
# ll.add_front('A')
# ll.add_front('A')
# ll.add_front('B')
# ll.add_front('C')
# ll.add_front('A')
# ll.add_end('F')

# print str(ll)
# print ll.size()
# print ll.kth_last(2)

# ll.remove_dup()
# print str(ll)
# print ll.size()


# nl = LinkList()

# nl.add_front(7)
# nl.add_front(3)
# nl.add_front(4)
# nl.add_front(6)
# nl.add_front(2)
# nl.add_front(1)
# nl.add_front(5)

# print str(nl)
# nl.part_by(4)
# print str(nl)