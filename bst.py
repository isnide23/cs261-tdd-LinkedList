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
      delete_me = self.search(value)
      #the bst is empty
      if delete_me is None:
         return self
      #the node is the root
      elif delete_me is self:
         if self.has_right_child:
            self = self.right.minimum()
         else:
            self = None
         return self
      #the node is a root with no children or a leaf node
      elif delete_me.is_leaf() is True:
         if delete_me.parent.left is delete_me:
            delete_me.parent.left = None
            delete_me = None
         else:
            delete_me.parent.right = None
            delete_me = None
         return self
      #the node has one child
      elif delete_me.is_leaf() is False:
         if delete_me.has_left_child():
            delete_me.parent.left = delete_me.left
            delete_me = delete_me.left
            return self
         elif delete_me.has_right_child():
            return self
         else:
            delete_me = None
            return self
      #the node has two children
      elif delete_me.has_two_children():
         replace_value = delete_me.right.minimum()
         # reset pointers to new node
         replace_value.left = delete_me.left
         replace_value.right = delete_me.right
         delete_me = replace_value
         self.delete(replace_value.key)
         return self
      #the BST is empty
      else:
         return None


      # node = self.search(value)
      # # node not found
      # if node is None:
      #    return self
      # # root node is being deleted
      # elif self.is_leaf() is True:
      #    node = None
      #    # if node.is_leaf() is True:
      #    #    node = None
      #    # elif node.has_two_children() is True or node.has_right_child() is True:
      #    #    new_node = node.right.minimum()
      #    #    node = new_node
      #    #    if node.has_left_child():
      #    #       left_child = node.left
      #    #       node.left = left_child
      #    # elif node.has_left_child() is True:
      #    #    node = node.left
      #    return node
      # # node is a leaf
      # elif node.is_leaf() is True:
      #    if node.parent.left is node:
      #       node.parent.left = None
      #    elif node.parent.right is node:
      #       node.parent.right = None
      #    return self
      # # node is not a leaf
      # elif node.is_leaf() is False:
      #    if node.has_two_children():
      #       return self
      #    elif node.has_left_child() is True:
      #       node = node.left
      #    elif node.has_right_child() is True:
      #       node = node.right.minimum()
      #    if self is node:
      #       self = node
      #    return self

   def keys(self, traverse_type):
      if traverse_type == 'pre':
         pass
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

   

         
      
   

