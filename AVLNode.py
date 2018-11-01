# Zybooks Implementation of AVLNode
class AVLNode(object):

  def __init__(self, key):
    self.key = key
    self.parent = None
    self.left = None
    self.right = None
    self.height = 0


  def get_balance(self):
    # Get current height of left subtree, or -1 if None
    left_height = -1
    if self.left is not None:
      left_height = self.left.height    
      # Get current height of right subtree, or -1 if None
    right_height = -1
    if self.right is not None:
      right_height = self.right.height
      # Calculate the balance factor.
    return left_height - right_height


  def update_height(self):
    # Get current height of left subtree, or -1 if None
    left_height = -1
    if self.left is not None:
      left_height = self.left.height      
      # Get current height of right subtree, or -1 if None
    right_height = -1
    if self.right is not None:
      right_height = self.right.height

     # Assign self.height with calculated node height.
    self.height = max(left_height, right_height) + 1


  def set_child(self, which_child, child):
    if which_child != "left" and which_child != "right":
      return False

    # Assign the left or right data member.
    if which_child == "left":
      self.left = child
    else:
      self.right = child

    # Assign the parent data member of the new child,
    # if the child is not None.
    if child is not None:
      child.parent = self

    # Update the node's height, since the subtree's structure
    # may have changed.
    self.update_height()
    return True


  def replace_child(self, current_child, new_child):
    if self.left is current_child:
      return self.set_child("left", new_child)
    elif self.right is current_child:
      return self.set_child("right", new_child)
    # If neither of the above cases applied, then the new child
    # could not be attached to this node.
    return False
