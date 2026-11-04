class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        return self.checkPath(root, 0, targetSum)

    def checkPath(self, node: TreeNode, current_sum: int, targetSum: int) -> bool:
        if node is None:
            return False
            
        current_sum = current_sum + node.val
        
        if node.left is None and node.right is None:
            if current_sum == targetSum:
                return True
            else:
                return False
                
        left_has = self.checkPath(node.left, current_sum, targetSum)
        right_has = self.checkPath(node.right, current_sum, targetSum)
        
        return left_has or right_has
