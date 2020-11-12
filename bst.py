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
      if value == self.key:
         return self
      elif value <= self.key and self.left is not None:
         return self.left.search(value)
      elif value > self.key and self.right is not None:
         return self.right.search(value)
      else:
         return None

   def delete(self, value):
      if value == self.search(value).key and self.search(value).is_leaf is True:
         self.search(value) == None
      elif value == self.search(value).key and self.search(value).is_leaf is False:
         self.search(value).minimum = self.search(value)
         self.search(value).minimum = None
      else:
         return None


   # def delete(self, value):
   #    if value == self.key:
   #       if self.right is not None:
   #          if self.left is not None:
   #             self.right.left = self.left
   #          self = self.right
   #          return self
   #       elif self.left is not None:
   #          self = self.left
   #          return self
   #       else:
   #          self = None
   #          return self
   #    elif self.left is not None and value == self.left.key:
   #       self.left = None
   #       return self
   #    elif self.right is not None and value == self.right.key:
   #       self.right = None
   #       return self
   #    else:
   #       return self

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
      if self.right is not None:
         return True
      else:
         return False

   def minimum(self):
      if self.left is None:
         return self
      elif self.left is not None:
         return self.left.minimum()

         
      
   

