# 1. Problem
Given the `root` of a binary tree and an integer `targetSum`, we need to return `True` if the tree has a root-to-leaf path where adding up all the node values along the path equals `targetSum`. Otherwise, return `False`.

# 2. Approach
I wrote a helper function `checkPath(node, current_sum, targetSum)` that keeps track of the running sum as we move down from the root:
1. If `root` is `None`, return `False` right away.
2. At each `node`, add `node.val` to `current_sum`.
3. Check if the current node is a leaf (`node.left is None and node.right is None`). If it is a leaf, check whether `current_sum == targetSum` and return `True` or `False`.
4. If it is not a leaf, recursively check the left subtree and the right subtree with the updated `current_sum`, and return `left_has or right_has`.

**Tracing with an example:**
Suppose the tree is `[5, 4, 8, 11, None]`, where `11` has left child `7` and right child `2`, and `targetSum = 22`:
- Start at `5`: `current_sum = 0 + 5 = 5`. Not a leaf. Call left (`4`) and right (`8`).
- At node `4`: `current_sum = 5 + 4 = 9`. Not a leaf (`4.left` is `11`). Call left (`11`).
- At node `11`: `current_sum = 9 + 11 = 20`. Not a leaf.
  - Call left (`7`): `current_sum = 20 + 7 = 27`. Node `7` is a leaf. `27 == 22` is `False`.
  - Call right (`2`): `current_sum = 20 + 2 = 22`. Node `2` is a leaf. `22 == 22` is `True`!
- Node `11` gets `False or True` -> returns `True` up to `4`, which returns `True` up to `5`.

**Challenges and failed attempts:**
In my first attempt, I tried checking `if current_sum == targetSum: return True` inside the base case `if node is None:`. That failed on two edge cases:
1. When the tree was empty (`root = []`) and `targetSum = 0`, my code returned `True` even though there are no nodes at all.
2. For the tree `[1, 2]` with `targetSum = 1`, node `1` had a left child `2` and no right child (`None`). When the recursion went to `1.right` (`None`), the running sum was `1`, so it returned `True` even though `1` is not a leaf node!
Checking the sum only when `node.left is None and node.right is None` fixed both problems.

# 3. Time Complexity
Time Complexity: O(n)

In the worst case, we have to visit every node in the tree to check all root-to-leaf paths. At each node we only do basic addition and comparisons (`O(1)`), so the total time complexity is `O(n)`.

# 4. Space Complexity
Space Complexity: O(h) (or O(n) in the worst case)

The algorithm only uses space for the recursive call stack, which equals the height of the tree `h`. In a skewed tree, `h = n` (`O(n)`), and in a balanced tree, `h = log n` (`O(log n)`).

# 5. Reflection / Improvement
- **Is there a more efficient approach?** Time and space complexity are already optimal (`O(n)` time and `O(h)` space).
- **What would you need to change?** The code can be simplified so it doesn't need a helper function or `current_sum` variable at all. Instead of adding up values from `0`, we can subtract `root.val` from `targetSum` on each recursive call (`self.hasPathSum(root.left, targetSum - root.val)`) and check `root.val == targetSum` at the leaf.
- **What complexity could the improved solution achieve?** It would keep the same `O(n)` time and `O(h)` space complexity, just with cleaner code.
