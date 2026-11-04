# 1. Problem
Given the `root` of a binary tree, we need to invert the tree (mirror it horizontally so every left child and right child are swapped) and return its root.

# 2. Approach
To mirror the whole tree, every single node needs to swap its left pointer and its right pointer.
1. If `root` is `None`, return `None`.
2. Save `root.left` in a temporary variable `temp`, set `root.left = root.right`, and set `root.right = temp`.
3. Recursively call `invertTree(root.left)` and `invertTree(root.right)` so the subtrees also swap their children all the way down.
4. Return `root`.

**Tracing with an example:**
Tree: `[4, 2, 7, 1, 3, 6, 9]`
- Iter 1 (at root `4`):
  - Swap `4.left` (`2`) and `4.right` (`7`). Now `4.left` is `7` and `4.right` is `2`.
  - Call `invertTree(7)` and `invertTree(2)`.
- Iter 2 (at node `7`):
  - Swap `7.left` (`6`) and `7.right` (`9`). Now `7.left` is `9` and `7.right` is `6`.
  - Call `invertTree(9)` and `invertTree(6)` -> their children are `None`, so they swap `None` with `None` and return.
- Iter 3 (at node `2`):
  - Swap `2.left` (`1`) and `2.right` (`3`). Now `2.left` is `3` and `2.right` is `1`.
  - Call `invertTree(3)` and `invertTree(1)` -> both are leaves and return.
- Final tree returned at root `4`: `[4, 7, 2, 9, 6, 3, 1]`.

**Challenges and failed attempts:**
In my first attempt, I didn't use a `temp` variable and wrote:
```python
root.left = self.invertTree(root.right)
root.right = self.invertTree(root.left)
```
When I tested it, the left side of the tree got copied onto both sides and the original left subtree completely disappeared! I realized that the first line overwrote `root.left` with the inverted right subtree, so on the second line `self.invertTree(root.left)` was actually inverting the same subtree again instead of the original left child. Using `temp = root.left` before swapping fixed the bug.

# 3. Time Complexity
Time Complexity: O(n)

We visit every node in the tree once and perform a constant-time pointer swap (`O(1)`) at each node. For `n` nodes, the total time complexity is `O(n)`.

# 4. Space Complexity
Space Complexity: O(h) (or O(n) in the worst case)

Since we swap pointers in place, we don't create any new tree nodes. The only extra space is the recursion call stack, which takes `O(h)` space where `h` is the height of the tree (`O(n)` for a skewed tree, `O(log n)` for a balanced tree).

# 5. Reflection / Improvement
- **Is there a more efficient approach?** `O(n)` time is optimal because every node's pointers must be swapped.
- **What would you need to change?** To avoid potential recursion depth issues on deep skewed trees, we could replace recursion with an iterative approach using a queue (BFS) or a stack, popping one node at a time and swapping its `left` and `right` children.
- **What complexity could the improved solution achieve?** Time complexity stays `O(n)` and space complexity is `O(n)` in the worst case, without relying on the call stack.
