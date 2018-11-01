# Zybooks implementation of AVLTree
import AVLNode as AVLNode

class AVLTree:

  def __init__(self):
    self.root = None


  def rotate_left(self, node):
    # Define a convenience pointer to the right child of the 
    # left child.
    right_left_child = node.right.left 
    # Step 1 - the right child moves up to the node's position.
    # This detaches node from the tree, but it will be reattached
    # later.
    if node.parent is not None:
      node.parent.replace_child(node, node.right)
    else:  # node is root
      self.root = node.right
      self.root.parent = None
    # Step 2 - the node becomes the left child of what used
    # to be its right child, but is now its parent. This will
    # detach right_left_child from the tree.
    node.right.set_child('left', node)
    # Step 3 - reattach right_left_child as the right child of node.
    node.set_child('right', right_left_child)
    return node.parent


  def rotate_right(self, node):
    # Define a convenience pointer to the left child of the 
    # right child.
    left_right_child = node.left.right
    # Step 1 - the left child moves up to the node's position.
    # This detaches node from the tree, but it will be reattached
    # later.
    if node.parent is not None:
      node.parent.replace_child(node, node.left)
    else:  # node is root
      self.root = node.left
      self.root.parent = None
    # Step 2 - the node becomes the right child of what used
    # to be its left child, but is now its parent. This will
    # detach left_right_child from the tree.
    node.left.set_child('right', node)
    # Step 3 - reattach left_right_child as the left child of node.
    node.set_child('left', left_right_child)
    return node.parent


  def rebalance(self, node):
    # First update the height of this node.
    node.update_height()        
    # Check for an imbalance.
    if node.get_balance() == -2:
      # The subtree is too big to the right.
      if node.right.get_balance() == 1:
        # Double rotation case. First do a right rotation
        # on the right child.
        self.rotate_right(node.right)
                
        # A left rotation will now make the subtree balanced.
      return self.rotate_left(node)
                        
    elif node.get_balance() == 2:

      # The subtree is too big to the left
      if node.left.get_balance() == -1:
        # Double rotation case. First do a left rotation
        # on the left child.
        self.rotate_left(node.left)
                
      # A right rotation will now make the subtree balanced.
      return self.rotate_right(node)
    # No imbalance, so just return the original node.
    return node
 

  def insert(self, node):
    # Special case: if the tree is empty, just set the root to
    # the new node.
    if self.root is None:
      self.root = node
      node.parent = None
    else:
      # Step 1 - do a regular binary search tree insert.
      current_node = self.root
      while current_node is not None:
        # Choose to go left or right
        if node.key < current_node.key:
          # Go left. If left child is None, insert the new
          # node here.
          if current_node.left is None:
            current_node.left = node
            node.parent = current_node
            current_node = None
          else:
            # Go left and do the loop again.
            current_node = current_node.left
        else:
          # Go right. If the right child is None, insert the
          # new node here.
          if current_node.right is None:
            current_node.right = node
            node.parent = current_node
            current_node = None
          else:
            # Go right and do the loop again.
            current_node = current_node.right
      # Step 2 - Rebalance along a path from the new node's parent up
      # to the root.
      node = node.parent
      while node is not None:
        self.rebalance(node)
        node = node.parent


  def remove_node(self, node):
    # Base case: 
    if node is None:
      return False
    # Parent needed for rebalancing.
    parent = node.parent
    # Case 1: Internal node with 2 children
    if node.left is not None and node.right is not None:
      # Find successor
      successor_node = node.right
      while successor_node.left != None:
        successor_node = successor_node.left
      # Copy the value from the node
      node.key = successor_node.key
      # Recursively remove successor
      self.remove_node(successor_node)
      # Nothing left to do since the recursive call will have rebalanced
      return True
    
    # Case 2: Root node (with 1 or 0 children)
    elif node is self.root:
      if node.left is not None:
        self.root = node.left
      else:
        self.root = node.right

      if self.root is not None:
        self.root.parent = None
      return True
    
    # Case 3: Internal with left child only
    elif node.left is not None:
      parent.replace_child(node, node.left)
    # Case 4: Internal with right child only OR leaf
    else:
      parent.replace_child(node, node.right)
    # node is gone. Anything that was below node that has persisted is already correctly
    # balanced, but ancestors of node may need rebalancing.
    node = parent
    while node is not None:
      self.rebalance(node)            
      node = node.parent
    return True


  def search(self, key):
    current_node = self.root
    while current_node is not None:
      # Compare the current node's key with the target key.
      # If it is a match, return the current key; otherwise go
      # either to the left or right, depending on whether the 
      # current node's key is smaller or larger than the target key.
      if current_node.key == key: return current_node
      elif current_node.key < key: current_node = current_node.right
      else: current_node = current_node.left
    return None


  def remove_key(self, key):
    node = self.search(key)
    if node is None:
      return False
    else:
      return self.remove_node(node)
