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
    self.contents = []
    
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
    def __repr__(self):
      if self.root is None:
        return("The tree is empty")
      else:
        self.print_tree(self.root)
        return (self.output)
  #Part 3: Add functionality to your BST class
  
  def add(self, input):
    if type(input) != int and type(input) != BSTNode:
      raise ValueError("Invalid input, please input either an integer or a BSTNode.")
    
    if type(input) == int:
      BSTNode(input)
    
    if input.data in self.contents:
      return

    if self.root == None:
      self.root == input
      self.contents.append(input.data)
      return

    self.add_node(self.root, input)
  
  def add_node(self, c_node, n_node):
    if n_node.data > c_node.data:
      if c_node.right == None:
        c_node.right = n_node
        self.contents.append(n_node.data)
        return
      else:
        self.add_node(c_node.right, n_node)
    else:
      if c_node.left == None:
        c_node.left = n_node
        self.contents.append(n_node.data)
        return
      else:
        self.add_node(c_node.left, n_node)
    


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
#create tree from image
node8 = BSTNode(8)
node3 = BSTNode(3)
node10 = BSTNode(10)
node1 = BSTNode(1)
node6 = BSTNode(6)
node14 = BSTNode(14)
node4 = BSTNode(4)
node7 = BSTNode(7)
node13 = BSTNode(13)

bst = BST()
bst.add(node8)
bst.add(node3)
bst.add(node10)
bst.add(node1)
bst.add(node6)
bst.add(node14)
bst.add(node4)
bst.add(node7)
bst.add(node13)