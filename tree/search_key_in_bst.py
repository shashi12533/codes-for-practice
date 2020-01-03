class getNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinaryTree:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return
        if root.data == val:
            return root
        if root.data > val:
            return self.searchBST(root.left, val)
        if root.data < val:
            return self.searchBST(root.right, val)
    def printnode(self,root):
        if root is None:
            return

        self.printnode(root.left)
        print(root.data)
        self.printnode(root.right)




if __name__ == '__main__':
    """ 
    Constructing below tree 
          2
          /\
          1  4
              /\
              3 7
     """
    tree = BinaryTree()
    root = getNode(2)  # 1
    root.left = getNode(1)  # / \
    root.right = getNode(4)  # 2 3
    root.right.left = getNode(3)
    root.right.right = getNode(7)

    k = 5
    t = tree.searchBST(root,k)
    tree.printnode(t)

# This code is c
