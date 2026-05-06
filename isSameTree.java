class Solution:
    def isSameTree(self, p, q):
        
        # Both are None
        if p is None and q is None:
            return True
        
        # One is None OR values different
        if p is None or q is None or p.val != q.val:
            return False
        
        # Check left and right subtree
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
