class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        self.traverse(root, result)
        return result

    def traverse(self, node: TreeNode, result: list[int]):
        if node is None:
            return
        self.traverse(node.left, result)
        self.traverse(node.right, result)
        result.append(node.val)
