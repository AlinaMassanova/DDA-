# 1. Problem
Given the `root` of a binary tree, find its minimum depth. The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node (a node with no children at all).

# 2. Approach
I solved this using recursion (DFS), similar to Maximum Depth, but with extra conditions for missing children:
1. If `root` is `None`, return `0`.
2. If both `root.left` and `root.right` are `None`, we reached a leaf node, so return `1`.
3. If `root.left` is `None`, we cannot take `0` from the left side because the current node is not a leaf. We must go down `root.right` and return `minDepth(root.right) + 1`.
4. Similarly, if `root.right` is `None`, we must go down `root.left` and return `minDepth(root.left) + 1`.
5. Only when both children exist, we compute `left_min` and `right_min` and return the smaller one plus `1`.

**Tracing with an example:**
Suppose the tree is `[2, None, 3, None, 4]` (a right-skewed chain `2 -> 3 -> 4`):
- Iter 1: `minDepth(2)` -> `2.left` is `None`, `2.right` is `3`. Hits `if root.left is None:` and calls `minDepth(3) + 1`.
- Iter 2: `minDepth(3)` -> `3.left` is `None`, `3.right` is `4`. Hits `if root.left is None:` and calls `minDepth(4) + 1`.
- Iter 3: `minDepth(4)` -> both `4.left` and `4.right` are `None`. Hits leaf base case and returns `1`.
- Unwinding:
  - `minDepth(3)` returns `1 + 1 = 2`.
  - `minDepth(2)` returns `2 + 1 = 3`.
Result is `3`.

**Challenges and failed attempts:**
My first attempt was just copying my `maxDepth` code and changing `>` to `<` (taking `min(left_depth, right_depth) + 1`). When I tested it on `[2, None, 3, None, 4, None, 5, None, 6]`, my code returned `1` instead of `5`! I realized why: node `2` had no left child, so `minDepth(2.left)` returned `0`, and `min(0, 4) + 1` gave `1`. But `2` is not a leaf node because it still has a right child. I had to explicitly handle the cases where one child is `None` before comparing both sides.

# 3. Time Complexity
Time Complexity: O(n)

With recursive DFS, the function visits every single node in the tree before returning the final minimum depth at the root. Therefore, it takes `O(n)` time.

# 4. Space Complexity
Space Complexity: O(h) (or O(n) in the worst case)

The space is used by the recursion call stack, which goes as deep as the height of the tree `h`. For a skewed tree of `n` nodes, this takes `O(n)` space.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** Yes! While worst-case Big-O time is still `O(n)`, my DFS approach is inefficient when a tree has one very shallow leaf on the left (say at depth 2) and a huge subtree of 10,000 nodes on the right. My DFS will still traverse all 10,000 nodes on the right even though the answer is 2.
- **What would you need to change?** Switch from recursive DFS to Breadth-First Search (BFS) using a queue. In BFS, we check nodes level by level from top to bottom. The very first node we encounter that has `left is None and right is None` is guaranteed to be at the minimum depth, and we can return immediately without checking the rest of the tree.
- **What complexity could the improved solution achieve?** Worst-case complexity remains `O(n)`, but in practice it runs in `O(b^d)` where `d` is the minimum depth, stopping as early as possible.
