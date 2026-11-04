# 1. Problem
Given the `root` of a binary tree, we need to find its maximum depth. The maximum depth is the number of nodes along the longest path from the root node all the way down to the farthest leaf node.

# 2. Approach
I used a recursive depth-first search (DFS) approach. The main idea is that the depth of any tree is just `1` (for the current root node) plus the maximum depth between its left subtree and its right subtree.

1. Base case: if `root` is `None`, the depth is `0`.
2. Recursively calculate `left_depth = self.maxDepth(root.left)` and `right_depth = self.maxDepth(root.right)`.
3. Compare `left_depth` and `right_depth`, take the larger one, and add `1` for the current node.

**Tracing with an example:**
Tree: `root = [3, 9, 20, None, None, 15, 7]`
- `maxDepth(3)` calls `maxDepth(9)` and `maxDepth(20)`.
- Inside `maxDepth(9)`:
  - `maxDepth(9.left)` -> `maxDepth(None)` returns `0`.
  - `maxDepth(9.right)` -> `maxDepth(None)` returns `0`.
  - Both are `0`, so `maxDepth(9)` returns `0 + 1 = 1`.
- Inside `maxDepth(20)`:
  - Calls `maxDepth(15)` -> both children of `15` are `None` (`0`), so `maxDepth(15)` returns `1`.
  - Calls `maxDepth(7)` -> both children of `7` are `None` (`0`), so `maxDepth(7)` returns `1`.
  - `left_depth` is `1` and `right_depth` is `1`, so `maxDepth(20)` returns `1 + 1 = 2`.
- Back at `maxDepth(3)`:
  - `left_depth` (from `9`) is `1`, `right_depth` (from `20`) is `2`.
  - Since `right_depth` is bigger, it returns `2 + 1 = 3`.

**Challenges and failed attempts:**
Initially, I got confused about whether a single root node with no children has depth `0` or `1` (counting edges vs counting nodes). At first, I added a base case `if not root.left and not root.right: return 0`, which gave an answer that was off by 1 for every non-empty tree. After re-reading the problem statement, I saw that depth counts the number of nodes on the path, so returning `0` only when `root is None` made everything work properly.

# 3. Time Complexity
Time Complexity: O(n)

The algorithm visits every node in the tree once to check the depths of both subtrees. At each node, comparing the two depths and adding 1 takes `O(1)` time, so the total time is `O(n)` where `n` is the number of nodes.

# 4. Space Complexity
Space Complexity: O(h) (or O(n) in the worst case)

We don't allocate any extra arrays, so the memory used comes only from the recursion call stack. The maximum number of active calls on the stack equals the height of the tree `h`. In the worst case (a skewed tree), `h = n`, so space complexity is `O(n)`. In a balanced tree, `h = log n`, so space is `O(log n)`.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** Both DFS and BFS must inspect every node to be sure which path is the longest, so `O(n)` time is optimal.
- **What would you need to change?** If the tree is extremely deep and skewed, recursion in Python could hit `RecursionError`. We could replace recursion with an iterative Breadth-First Search (BFS) using a queue to count levels one by one.
- **What complexity could the improved solution achieve?** Iterative BFS still has `O(n)` time and `O(n)` worst-case space (for the widest level in the queue), but it avoids call stack overflow.
