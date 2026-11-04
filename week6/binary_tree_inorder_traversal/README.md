# 1. Problem
We are given the `root` of a binary tree and need to return a list of its node values in inorder traversal order. Inorder means we first visit the left subtree, then the current node itself, and finally the right subtree.

# 2. Approach
I solved this using recursion with a separate helper method. In `inorderTraversal`, I create an empty list called `result` and pass it into `helper(node, result)`.

Inside the helper method:
1. If the current `node` is `None`, I just return and do nothing.
2. Otherwise, I first call `helper(node.left, result)` to process everything on the left side.
3. Then I append `node.val` to `result`.
4. Finally, I call `helper(node.right, result)` to process everything on the right side.

**Tracing with an example:**
Suppose the tree is `root = [1, None, 2, 3]` (root is `1`, right child of `1` is `2`, left child of `2` is `3`):
- Step 1: Call `helper(1, [])`.
  - First go left: `helper(None, [])` -> hits base case and returns immediately.
  - Append `1` to `result` -> `result` is now `[1]`.
  - Next go right: call `helper(2, [1])`.
- Step 2: Inside `helper(2, [1])`:
  - Go left: call `helper(3, [1])`.
- Step 3: Inside `helper(3, [1])`:
  - Go left: `helper(None, [1])` -> returns.
  - Append `3` to `result` -> `result` is now `[1, 3]`.
  - Go right: `helper(None, [1, 3])` -> returns.
- Step 4: Back inside `helper(2, [1, 3])`:
  - Left side of `2` is done, so append `2` -> `result` is now `[1, 3, 2]`.
  - Go right of `2`: `helper(None, [1, 3, 2])` -> returns.
- Step 5: All recursive calls finish, and we return `[1, 3, 2]`.

**Challenges and failed attempts:**
At first, I tried initializing `result = []` inside the main `inorderTraversal` function without a helper function and calling `inorderTraversal` recursively. The problem was that `result = []` got reset to an empty list on every recursive call, so at the end I only got the root value or lost the values from the subtrees. Moving the recursion into a separate `helper` function that receives the same `result` list fixed this issue.

# 3. Time Complexity
Time Complexity: O(n)

Every node in the binary tree is visited exactly once. At each node, we only do a constant amount of work (checking for `None` and appending the value to the list), so the total time grows linearly with the number of nodes `n`.

# 4. Space Complexity
Space Complexity: O(n)

We store `n` values in the `result` list, and the recursion call stack also takes memory depending on the height of the tree. In the worst case (when the tree is completely skewed like a linked list), the recursion stack reaches a depth of `n`, giving `O(n)` space. For a balanced tree, the stack space is `O(log n)`.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** In terms of time complexity, `O(n)` cannot be beat because we have to read every node at least once. However, the extra space used by the recursion stack can be improved.
- **What would you need to change?** To avoid recursion limits, we could use an iterative approach with an explicit stack (`while` loop). If we wanted to reduce the auxiliary space even further, we could use Morris Traversal, which temporarily modifies tree pointers to traverse without a stack.
- **What complexity could the improved solution achieve?** Morris Traversal achieves `O(n)` time complexity and `O(1)` auxiliary space (excluding the output list).
