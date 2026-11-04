class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
            
        if root.left is None:
            return self.minDepth(root.right) + 1
            
        if root.right is None:
            return self.minDepth(root.left) + 1
            
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        
        if left_min < right_min:
            return left_min + 1
        else:
            return right_min + 1
