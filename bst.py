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
            child.parent = self.left
            return
         else:
            self.right.insert(child)
            child.parent = self.right
            return
      
         
   def search(self, value):
      if value == self.key:
         return self
      else:
         return None

   def delete(self, value):
      if self.key == value:
         return None
      else:
         return self
   

