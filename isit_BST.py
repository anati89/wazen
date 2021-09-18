""" Program to check if a given Binary
Tree is balanced like a Red-Black Tree """

# Helper function that allocates a new
# node with the given data and None
# left and right poers.								
class newNode:

	# Construct to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Returns true if given tree is BST.
def isBST(root, l, r, root_val):
    if l:
        if l.data > root.data or l.data > root_val:
	        return False
    if r:
        if r.data < root.data or r.data < root_val:
	        return False
    l_flag = isBST(l, l.left, l.right, root_val) if l else True
    r_flag = isBST(r, r.left, r.right, root_val) if r else True
    return l_flag and r_flag

# Driver Code
if __name__ == '__main__':
	root = newNode(3)
	root.left = newNode(2)
	root.right = newNode(5)
	root.right.left = newNode(1)
	root.right.right = newNode(4)
	#root.right.left.left = newNode(40)
	root_val = root.data
	if (isBST(root, root.left, root.right, root_val)):
		print("Is BST")
	else:
		print("Not a BST")

# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)
