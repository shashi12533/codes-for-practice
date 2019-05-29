binary-tree-maximum-path-sum/


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            nodemax = max(node.val + left, node.val+ right, node.val,node.val+left+right)
            if nodemax > self.max:
                self.max = nodemax
            return max(node.val, node.val+left, node.val+right)
        
        
        if not root: return 0
        self.max = root.val
        traverse(root)        
        return self.max 

