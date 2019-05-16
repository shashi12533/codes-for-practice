invert binary tree

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is not None and root.val is not None:
            t = root.left
            root.left = root.right
            root.right = t
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root
