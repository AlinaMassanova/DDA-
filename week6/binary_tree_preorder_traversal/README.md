# 1. Problem
Given the `root` of a binary tree, return the preorder traversal of its nodes' values. In preorder traversal, we visit the current root node first, then all nodes in the left subtree, and finally all nodes in the right subtree.

# 2. Approach
I wrote a direct recursive function without a helper method by combining lists:
1. If `root` is `None`, return an empty list `[]`.
2. Recursively get the list of values from the left subtree (`left_values`) and the right subtree (`right_values`).
3. Concatenate `[root.val] + left_values + right_values` and return the combined list.

**Tracing with an example:**
Tree: `root = [1, 2, 3]`, where `2` has left child `4`:
- Call `preorderTraversal(1)`:
  - Calls `preorderTraversal(2)`:
    - Calls `preorderTraversal(4)` -> both children of `4` are `None` (return `[]`), so `4` returns `[4] + [] + [] = [4]`.
    - Calls `preorderTraversal(2.right)` (`None`) -> returns `[]`.
    - Node `2` returns `[2] + [4] + [] = [2, 4]`.
  - Calls `preorderTraversal(3)`:
    - Both children of `3` are `None` (`[]`), so `3` returns `[3] + [] + [] = [3]`.
  - Node `1` combines everything: `[1] + [2, 4] + [3] = [1, 2, 4, 3]`.

**Challenges and failed attempts:**
At first I tried writing `return root.val + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)`, which threw a `TypeError` because `root.val` is an integer and cannot be added directly to a `list`. Wrapping `root.val` inside square brackets `[root.val]` fixed the type mismatch.

# 3. Time Complexity
Time Complexity: O(n^2) in the worst case (O(n log n) for a balanced tree)

Even though there are `n` recursive calls (one per node), list concatenation `[root.val] + left_values + right_values` creates a brand new list and copies all elements from `left_values` and `right_values` at every step. If the tree is skewed like a linked list of length `n`, copying lists of sizes `1, 2, 3, ..., n` takes `1 + 2 + ... + n = O(n^2)` time.

# 4. Space Complexity
Space Complexity: O(n)

We store the final list of `n` elements, and the recursion stack takes `O(h)` space (up to `O(n)` in a skewed tree), plus temporary list copies created during concatenation.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** Yes. Creating new lists with `+` at every node wastes time copying elements over and over.
- **What would you need to change?** Instead of concatenating lists with `+`, we can either pass a single shared `result` list into a helper function and use `result.append(node.val)` (which is `O(1)`), or use an iterative approach with an explicit stack where we push the right child then the left child.
- **What complexity could the improved solution achieve?** Using `.append()` on a single list or an iterative stack improves the time complexity from `O(n^2)` down to `O(n)`.
