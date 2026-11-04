class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.dfs(root, False)

    def dfs(self, node: TreeNode, is_left: bool) -> int:
        if node is None:
            return 0
            
        if node.left is None and node.right is None:
            if is_left:
                return node.val
            else:
                return 0
                
        left_sum = self.dfs(node.left, True)
        right_sum = self.dfs(node.right, False)
        
        return left_sum + right_sum
