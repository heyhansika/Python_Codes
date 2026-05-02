class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        
        # If left is None → go right
        if not root.left:
            return 1 + self.minDepth(root.right)
        
        # If right is None → go left
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # If both exist → take minimum
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
