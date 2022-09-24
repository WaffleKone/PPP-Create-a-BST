#Part 1: Create a BSTNode class
class BSTNode():
  def __init__(self, data=None, left=None, right=None):
    self.data = data
    self.left = left
    self.right = right
  def __str__(self):
    return (f"{self.data}")
  def __repr__(self):
      return (f"{self.data}")
#Part 2: Create a BST class
class BST():
  def __init__(self, root=None):
    self.root = root
    self.output = ""
    
  def print_tree(self, node, level=0):
    if node != None:
      self.print_tree(node.right, level + 1)
      self.output += ' ' * 4 * level + '-> ' + str(node.data) + ''
      self.print_tree(node.left, level + 1)

  def __str__(self):
    if self.root is None:
      return("The tree is empty")
    else:
      self.print_tree(self.root)
      return (self.output)
  #Part 3: Add functionality to your BST class



# Testing
node1 = BSTNode(3)
print(node1) #3

node2 = BSTNode(4, left=node1)
print(node2) #4

node3 = BSTNode()
print(node3) #None
node3.data = 5
print(node3) #5
bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)
