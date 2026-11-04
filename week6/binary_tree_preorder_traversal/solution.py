class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
            
        left_values = self.preorderTraversal(root.left)
        right_values = self.preorderTraversal(root.right)
        
        return [root.val] + left_values + right_values
