# BinarySearchTree: A binary search tree.
# Implement as many operations as possible with recursion.
# If you can't figure it out recursively, use a loop. (But then refactor
# your implementation into a recursive one!)
# Your implementation should pass the tests in test_bst.py.
# Ian Snyder

class BinarySearchTree:

   def __init__(self, key = None):
      self.left = None
      self.right = None
      self.key = key
      self.parent = None
      self.root = self
      

   def insert(self, child):
      if child.key <= self.key and self.left == None:
         self.left = child
         child.parent = self
         return
      elif child.key > self.key and self.right == None:
         self.right = child
         child.parent = self
         return
      else:
         if child.key <= self.key:
            self.left.insert(child)
            return
         else:
            self.right.insert(child)
            return
      
         
   def search(self, value):
      #the root contains the search value
      if value == self.key:
         return self
      #the value is less than the root value
      elif value < self.key and self.left is not None:
         return self.left.search(value)
      #the value is greater than the root value
      elif value > self.key and self.right is not None:
         return self.right.search(value)
      #the value is not found
      else:
         return None

   def delete(self, value):
      node = self.search(value)
      #the bst is empty
      if node is None:
         return self
      #the node is a root with no children or a leaf node
      elif node.is_leaf() is True:
         if node.is_root() is True:
            self = None
         elif node.parent.right is node:
            node.parent.right = None
            node = None
         else:
            node.parent.left = None
            node = None
         return self
      #the node has one child
      elif node.has_one_child():
         if node.is_root() is True:
            if node.has_left_child(): 
               node = node.left
               return node
            else:
               node = node.right
               return node
         elif node.has_left_child():
            node.parent.left = node.left
            node = node.left
            return self
         elif node.has_right_child():
            return self
         else:
            node = None
            return self
      #the node has two children
      elif node.has_two_children() and node.is_root():
         min = node.right.minimum()
         min.left = node.left
         if node.right is not min:
            min.right = node.right
         self = min
         if min.parent.left == min:
            min.parent.left = None
         return self
      elif node.has_two_children():
         min = node.right.minimum()
         min.left = node.left
         if node.right is not None and node.right is not min:
            min.right = node.right
         if node.parent.left == node:
            node.parent.left = min
         else:
            node.parent.right = min
         node = min
         if min.parent.left == min:
            min.parent.left = None
         elif min.parent.right == None:
            min.parent.right = None
         
         return self
      #the BST is empty
      else:
         return None

   def keys(self, traverse_type):
      keys = []
      if traverse_type == 'pre':
         keys.append(self.key)
         if self.left is not None:
            keys.extend(self.left.keys('pre'))
            
            # return keys
         #elif self.right is not None:
            keys.extend(self.right.keys('pre'))
         return keys
      elif traverse_type == 'in':
         pass
      elif traverse_type == 'post':
         pass
      else:
         return None

   def is_leaf(self):
      if self.left is None and self.right is None:
         return True
      else:
         return False

   def has_left_child(self):
      if self.left is not None:
         return True
      else:
         return False
      
   def has_right_child(self):
      return self.right is not None
      # if self.right is not None:
      #    return True
      # else:
      #    return False

   def has_one_child(self):
      if self.left is not None and self.right is None:
         return True
      elif self.left is None and self.right is not None:
         return True
      else:
         return False

   def has_two_children(self):
      if self.left is not None and self.right is not None:
         return True
      else:
         return False

   def is_root(self):
      return self.parent is None

   def minimum(self):
      if self.left is None:
         return self
      else:
         return self.left.minimum()

   def less_than_three_levels(self):
      return self.left.is_leaf() and self.right.is_leaf() 

   

         
      
   

