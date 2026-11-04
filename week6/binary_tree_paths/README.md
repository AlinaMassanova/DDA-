# 1. Problem
Given the `root` of a binary tree, we need to return all root-to-leaf paths as strings formatted with `"->"` between node values (for example, `"1->2->5"`).

# 2. Approach
I created a helper function `findPaths(node, current_path, paths)` that builds the path string as we go down from the root:
1. Start with `current_path = ""` and an empty list `paths = []`.
2. At each node, if `current_path` is empty (which happens at the root), set `current_path = str(node.val)`. Otherwise, append `"->" + str(node.val)` to `current_path`.
3. If the current node is a leaf (`node.left is None and node.right is None`), append `current_path` to `paths` and return.
4. Otherwise, recursively call `findPaths` on `node.left` and `node.right`, passing the updated `current_path`. Because strings in Python are immutable, each recursive call gets its own copy of `current_path` without messing up the other branch.

**Tracing with an example:**
Tree: `root = [1, 2, 3, None, 5]` (`1` has children `2` and `3`, and `2` has right child `5`):
- Step 1: `findPaths(1, "", paths)`
  - `current_path` becomes `"1"`. Not a leaf.
  - Calls `findPaths(2, "1", paths)` and `findPaths(3, "1", paths)`.
- Step 2: Inside `findPaths(2, "1", paths)`:
  - `current_path` becomes `"1->2"`. Not a leaf (`2.right` is `5`).
  - Calls `findPaths(None, "1->2", paths)` -> returns immediately.
  - Calls `findPaths(5, "1->2", paths)`.
- Step 3: Inside `findPaths(5, "1->2", paths)`:
  - `current_path` becomes `"1->2->5"`.
  - Both children of `5` are `None` (leaf!), so `"1->2->5"` is appended to `paths`.
- Step 4: Inside `findPaths(3, "1", paths)`:
  - `current_path` becomes `"1->3"`.
  - Both children of `3` are `None` (leaf!), so `"1->3"` is appended to `paths`.
- Result: `["1->2->5", "1->3"]`.

**Challenges and failed attempts:**
At first, I always did `current_path = current_path + str(node.val) + "->"` at every node, which left an extra `"->"` hanging at the end of every path like `"1->2->5->"`. Then I tried only adding `"->"` before `str(node.val)`, which put a leading arrow at the start (`"->1->2->5"`). Adding the check `if current_path == "":` for the root node solved the formatting cleanly.

# 3. Time Complexity
Time Complexity: O(n * h) (which is O(n^2) in the worst case, or O(n log n) for a balanced tree)

We visit all `n` nodes, and at each node we concatenate `current_path + "->" + str(node.val)`. Because Python strings are immutable, creating a new string copies all characters in `current_path` so far (which has length proportional to depth `h`). In a skewed tree of `n` nodes, string concatenation takes `1 + 2 + ... + n = O(n^2)` time.

# 4. Space Complexity
Space Complexity: O(n * h)

The recursion call stack reaches depth `h`, and at each depth frame on the stack we hold a separate `current_path` string of length up to `O(h)`, plus the output list `paths` storing all root-to-leaf path strings.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** Yes, creating a new string via concatenation at every single step down the tree does unnecessary copying on intermediate nodes.
- **What would you need to change?** Instead of passing a string `current_path`, we can pass a single Python list `path = []`, do `path.append(str(node.val))` when entering a node, and `path.pop()` (backtracking) when leaving the node. We would only call `"->".join(path)` when we actually reach a leaf node.
- **What complexity could the improved solution achieve?** Backtracking with a list avoids copying strings on internal nodes, so intermediate work per node becomes `O(1)` and string building only happens at the leaves.
