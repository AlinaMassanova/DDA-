class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        paths = []
        if root is None:
            return paths
        self.findPaths(root, "", paths)
        return paths

    def findPaths(self, node: TreeNode, current_path: str, paths: list[str]):
        if node is None:
            return
            
        if current_path == "":
            current_path = str(node.val)
        else:
            current_path = current_path + "->" + str(node.val)
            
        if node.left is None and node.right is None:
            paths.append(current_path)
            return
            
        self.findPaths(node.left, current_path, paths)
        self.findPaths(node.right, current_path, paths)
