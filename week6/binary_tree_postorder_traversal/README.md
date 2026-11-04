# 1. Problem
Given the `root` of a binary tree, we need to return the postorder traversal of its nodes' values. In postorder traversal, we visit the left subtree first, then the right subtree, and visit the current node last.

# 2. Approach
I used a recursive helper method `traverse(node, result)`:
1. Create an empty list `result` in `postorderTraversal`.
2. In `traverse`, if `node` is `None`, return immediately.
3. Recursively traverse `node.left`.
4. Recursively traverse `node.right`.
5. After both subtrees are completely processed, append `node.val` to `result`.

**Tracing with an example:**
Suppose the tree is `[1, None, 2, 3]` (`1` has right child `2`, and `2` has left child `3`):
- Step 1: Call `traverse(1, [])`.
  - Left child of `1` is `None` -> `traverse(None, [])` returns.
  - Right child of `1` is `2` -> call `traverse(2, [])`.
- Step 2: Inside `traverse(2, [])`:
  - Left child of `2` is `3` -> call `traverse(3, [])`.
- Step 3: Inside `traverse(3, [])`:
  - `3.left` is `None` -> returns.
  - `3.right` is `None` -> returns.
  - Append `3` -> `result` is `[3]`.
- Step 4: Back inside `traverse(2, [3])`:
  - `2.right` is `None` -> returns.
  - Both children of `2` are done, so append `2` -> `result` is `[3, 2]`.
- Step 5: Back inside `traverse(1, [3, 2])`:
  - Both children of `1` are done, so append `1` -> `result` is `[3, 2, 1]`.
Return `[3, 2, 1]`.

**Challenges and failed attempts:**
Before using recursion, I tried to write an iterative solution with a `while` loop and a stack like I saw for preorder traversal. However, in postorder you cannot pop and record a parent node until both of its children have already been visited, so my loop kept pushing the children back onto the stack in an infinite loop. Switching to recursion made the `Left -> Right -> Root` order much easier to express without needing extra visited flags.

# 3. Time Complexity
Time Complexity: O(n)

Each node in the tree is visited once, and `result.append(node.val)` takes `O(1)` time per node. For `n` nodes, the total time is `O(n)`.

# 4. Space Complexity
Space Complexity: O(n)

The `result` list stores `n` integers, and the recursion stack uses `O(h)` space where `h` is the height of the tree. In the worst case of a skewed tree, the stack takes `O(n)` space.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** `O(n)` time is optimal since every node must be visited.
- **What would you need to change?** If we wanted to avoid recursion to prevent stack overflow on very deep trees, we could implement an iterative version. A neat trick is to do a modified preorder traversal in the order `Root -> Right -> Left` using a stack, and then reverse the result list at the end (`result[::-1]`) to get `Left -> Right -> Root`.
- **What complexity could the improved solution achieve?** It would run in `O(n)` time and `O(h)` explicit stack space without using the system call stack.
