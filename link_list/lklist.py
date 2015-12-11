
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
        
        
class LinkList:

  def __init__(self):
    self.head = None
    
  def __str__(self):
    string = ""
    if self.is_empty():
      return string
      
    current = self.head
    string += current.get_data()
    while(current.get_next() != None):
      current = current.get_next()
      string += '->'+str(current)
    return string
    
  def is_empty(self):
    return(self.head == None)
    
  def add_front(self, item):
    temp = Node(item, self.head)
    self.head = temp
    
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
      
    
ll = LinkList()
ll.add_front('B')
ll.add_front('A')
ll.add_front('A')
ll.add_front('B')
ll.add_front('C')
ll.add_front('A')

print str(ll)
ll.remove_dup()
print str(ll)