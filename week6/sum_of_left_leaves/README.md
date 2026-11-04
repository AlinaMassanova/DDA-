# 1. Problem
Given the `root` of a binary tree, return the sum of all left leaves. A leaf is a node with no children, and a left leaf is a leaf that is the left child of its parent.

# 2. Approach
When we are standing at a leaf node, the node itself does not know whether it was the left child or right child of its parent. To solve this, I wrote a helper function `dfs(node, is_left)` that passes a boolean flag `is_left`:
1. Start from the root with `dfs(root, False)` because the root itself is not a left child.
2. If `node` is `None`, return `0`.
3. If `node` is a leaf (`node.left is None and node.right is None`), check `is_left`. If `is_left` is `True`, return `node.val`; otherwise return `0`.
4. For non-leaf nodes, call `dfs(node.left, True)` (passing `True` because we are moving to a left child) and `dfs(node.right, False)` (passing `False` because we are moving to a right child), and return the sum of both results.

**Tracing with an example:**
Tree: `root = [3, 9, 20, None, None, 15, 7]`
- Start: `dfs(3, False)` -> not a leaf. Calls `dfs(9, True)` and `dfs(20, False)`.
- Inside `dfs(9, True)`:
  - `9.left` is `None` and `9.right` is `None` (leaf!).
  - `is_left` is `True`, so it returns `9`.
- Inside `dfs(20, False)`:
  - Not a leaf. Calls `dfs(15, True)` and `dfs(7, False)`.
  - Inside `dfs(15, True)`: leaf and `is_left` is `True` -> returns `15`.
  - Inside `dfs(7, False)`: leaf, but `is_left` is `False` -> returns `0`.
  - `dfs(20, False)` returns `15 + 0 = 15`.
- Back at root `3`: returns `9 + 15 = 24`.

**Challenges and failed attempts:**
At first, I misread the problem and added `node.left.val` whenever `node.left` existed. That failed whenever a left child had its own children (because then it is an internal node, not a leaf). Also, for a tree with just a single root node `[1]`, I initially returned `1` before realizing the root has no parent and is not a left leaf. Passing `False` for the root in `self.dfs(root, False)` handled that edge case properly.

# 3. Time Complexity
Time Complexity: O(n)

Every node in the binary tree is visited once during the depth-first search, and we do `O(1)` work at each node. Total time is `O(n)`.

# 4. Space Complexity
Space Complexity: O(h) (or O(n) in the worst case)

The space complexity comes from the recursion call stack, which grows up to the height `h` of the tree (`O(n)` for a skewed tree, `O(log n)` for a balanced tree).

# 5. Reflection / Improvement
- **Is there a more efficient approach?** `O(n)` time and `O(h)` space are already optimal for recursive traversal.
- **What would you need to change?** We could eliminate the helper function `dfs` and the `is_left` boolean parameter by checking from the parent node directly: `if root.left and root.left.left is None and root.left.right is None: total += root.left.val`.
- **What complexity could the improved solution achieve?** It would keep the same `O(n)` time and `O(h)` space complexity with slightly fewer function arguments.
