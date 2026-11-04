# 1. Problem
Given the `head` of a linked list, we need to check whether the linked list has a cycle in it. A cycle happens when some node's `next` pointer points back to an earlier node in the list, so following `.next` never reaches `None`.

# 2. Approach
I solved this by keeping track of every node I have already visited using a `set`:
1. Create an empty set called `visited` and a pointer `current = head`.
2. Loop while `current` is not `None`.
3. At each step, check if `current` is already inside `visited`. If it is, that means we came back to the exact same node a second time, so there is a cycle and we return `True`.
4. Otherwise, add `current` to `visited` and move forward with `current = current.next`.
5. If `current` reaches `None`, the list has an end, so there is no cycle and we return `False`.

**Tracing with an example:**
Suppose the list is `[3, 2, 0, -4]` where `-4.next` points back to node `2`:
- Start: `visited = {}`, `current` is at node `3`.
- Iteration 1: node `3` is not in `visited`. Add node `3` to `visited`. Move `current` to node `2`.
- Iteration 2: node `2` is not in `visited`. Add node `2` to `visited`. Move `current` to node `0`.
- Iteration 3: node `0` is not in `visited`. Add node `0` to `visited`. Move `current` to node `-4`.
- Iteration 4: node `-4` is not in `visited`. Add node `-4` to `visited`. Move `current` to `-4.next`, which is node `2`.
- Iteration 5: `current` is node `2`. Check `if current in visited` -> `True` because node `2` was added in Iteration 2! Return `True`.

**Challenges and failed attempts:**
In my first attempt, I stored `current.val` (the integer value) in `visited` instead of the `current` node object itself. That failed on lists that had duplicate numbers without a cycle (for example `[1, 2, 1]`), because seeing the number `1` twice made my code think there was a cycle. Changing `visited.add(current.val)` to `visited.add(current)` fixed it because two different nodes with the same value are still different objects in memory.

# 3. Time Complexity
Time Complexity: O(n)

We visit each of the `n` nodes at most once. Checking if a node is in a Python `set` (`current in visited`) and adding it (`visited.add(current)`) both take `O(1)` average time, so the total time is `O(n)`.

# 4. Space Complexity
Space Complexity: O(n)

Because we store every visited node in the `visited` set, if the linked list has `n` nodes, the set will hold up to `n` node references in memory.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** Yes, we can improve the space complexity so we don't need a `set` at all.
- **What would you need to change?** Instead of storing visited nodes in a set, we can use two pointers (`slow` and `fast`, also called Floyd's Tortoise and Hare algorithm). `slow` moves 1 step at a time (`slow = slow.next`) and `fast` moves 2 steps at a time (`fast = fast.next.next`). If there is a cycle, `fast` will eventually lap `slow` and they will meet at the same node.
- **What complexity could the improved solution achieve?** The two-pointer approach keeps `O(n)` time complexity while reducing the space complexity from `O(n)` down to `O(1)`.
