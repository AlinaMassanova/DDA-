# 1. Problem
We are given the roots of two binary trees, `root1` and `root2`. We need to merge them into a single binary tree by overlapping them: if two nodes occupy the same position, their values are summed up; if only one node exists at a position, we use that non-null node directly.

# 2. Approach
I used recursion to walk through both trees at the same time and build a merged node whenever both exist:
1. If both `root1` and `root2` are `None`, return `None`.
2. If `root1` is `None`, return `root2` (which attaches the rest of `root2`'s subtree as-is).
3. If `root2` is `None`, return `root1`.
4. If both nodes exist, create a new node `merged = TreeNode(root1.val + root2.val)`.
5. Recursively set `merged.left = self.mergeTrees(root1.left, root2.left)` and `merged.right = self.mergeTrees(root1.right, root2.right)`, then return `merged`.

**Tracing with an example:**
Suppose `root1 = [1, 3, 2, 5]` (`1` has left `3`, right `2`; `3` has left `5`) and `root2 = [2, 1, 3, None, 4, None, 7]` (`2` has left `1`, right `3`; `1` has right `4`; `3` has right `7`):
- Step 1: `mergeTrees(1, 2)` -> both exist, so create `TreeNode(1 + 2 = 3)`.
  - Call left: `mergeTrees(3, 1)`.
  - Call right: `mergeTrees(2, 3)`.
- Step 2: Inside `mergeTrees(3, 1)`:
  - Both exist -> create `TreeNode(3 + 1 = 4)`.
  - Left of `(3, 1)`: `mergeTrees(5, None)` -> `root2` is `None`, so it returns node `5` directly.
  - Right of `(3, 1)`: `mergeTrees(None, 4)` -> `root1` is `None`, so it returns node `4` directly.
  - Node `4` now has left child `5` and right child `4`.
- Step 3: Inside `mergeTrees(2, 3)`:
  - Both exist -> create `TreeNode(2 + 3 = 5)`.
  - Left of `(2, 3)`: `mergeTrees(None, None)` -> returns `None`.
  - Right of `(2, 3)`: `mergeTrees(None, 7)` -> `root1` is `None`, returns node `7`.
  - Node `5` now has left `None` and right `7`.
- Final merged tree: `[3, 4, 5, 5, 4, None, 7]`.

**Challenges and failed attempts:**
Initially, when `root1` was `None` and `root2` was not `None`, I still tried to create a new `TreeNode(0 + root2.val)` and keep recursing on `root1.left` and `root2.left`. That crashed with `AttributeError: 'NoneType' object has no attribute 'left'` because `root1` was `None`! Then I realized that if `root1` is `None`, we don't even need to traverse the rest of `root2`'s subtree—we can just return `root2` right away since all of its children are already connected.

# 3. Time Complexity
Time Complexity: O(min(n, m))

Here `n` and `m` are the number of nodes in `root1` and `root2`. We only recurse deeper when both `root1` and `root2` are non-null at the current position. As soon as one of them is `None`, we return the other node in `O(1)` time. So we only visit the overlapping nodes between the two trees.

# 4. Space Complexity
Space Complexity: O(min(n, m))

Because my solution creates a new `TreeNode` for every overlapping node between `root1` and `root2`, it allocates up to `min(n, m)` new nodes in memory, in addition to the recursion call stack of depth `O(min(h1, h2))`.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** The time complexity `O(min(n, m))` is already optimal, but the space complexity can be improved.
- **What would you need to change?** Instead of creating a brand new `TreeNode(root1.val + root2.val)` at every step, we can modify `root1` in place by writing `root1.val += root2.val`, updating `root1.left` and `root1.right`, and returning `root1`.
- **What complexity could the improved solution achieve?** Modifying `root1` in place avoids allocating any new `TreeNode` objects, reducing the space complexity to `O(min(h1, h2))` for the recursion stack only.
