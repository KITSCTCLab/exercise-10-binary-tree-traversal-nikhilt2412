class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    p = BinaryTreeNode(new_value)
    
    if root == None:
        root = p
    
    else:
        temp = root
        while temp.right_child != None or temp.left_child != None:
            if temp.data > new_value:
                temp = temp.left_child
            else:
                temp = temp.right_child
        if temp.data > new_value:
                temp.left_child = p
        else:
                temp.right_child = p

    return root

def inorder(self, root) -> None:
    # Write your code here
        res = []
        
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
            return res
        
def preorder(root) -> None:
    # Write your code here


def postorder(root) -> None:
    # Write your code here


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
