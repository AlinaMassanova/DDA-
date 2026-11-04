# 1. Problem
We are given the heads of two sorted linked lists, `list1` and `list2`. We need to merge them into a single sorted linked list by connecting their nodes together and return the head of the merged list.

# 2. Approach
I used a `dummy` starter node and a `current` pointer to build the merged list step by step:
1. Create `dummy = ListNode(0)` and set `current = dummy`. Having a dummy node makes it easy to attach the first node without writing extra `if` conditions for setting the head.
2. While both `list1` and `list2` still have nodes, compare `list1.val` and `list2.val`.
3. If `list1.val <= list2.val`, attach `list1` to `current.next` and move `list1` to `list1.next`. Otherwise, attach `list2` to `current.next` and move `list2` to `list2.next`.
4. Advance `current = current.next` after each step.
5. Once one of the lists becomes `None`, attach the remaining part of the other list directly to `current.next`.
6. Return `dummy.next`, which points to the real head of our merged list.

**Tracing with an example:**
Suppose `list1 = [1, 2, 4]` and `list2 = [1, 3, 4]`:
- Start: `dummy(0)`, `current` is at `dummy`.
- Iteration 1: compare `1` (`list1`) and `1` (`list2`). `1 <= 1`, so `current.next` becomes `1` from `list1`. `list1` moves to `2`, `current` moves to `1`.
- Iteration 2: compare `2` (`list1`) and `1` (`list2`). `2 > 1`, so `current.next` becomes `1` from `list2`. `list2` moves to `3`, `current` moves to `1`.
- Iteration 3: compare `2` (`list1`) and `3` (`list2`). `2 <= 3`, so `current.next` becomes `2` from `list1`. `list1` moves to `4`, `current` moves to `2`.
- Iteration 4: compare `4` (`list1`) and `3` (`list2`). `4 > 3`, so `current.next` becomes `3` from `list2`. `list2` moves to `4`, `current` moves to `3`.
- Iteration 5: compare `4` (`list1`) and `4` (`list2`). `4 <= 4`, so `current.next` becomes `4` from `list1`. `list1` becomes `None`, `current` moves to `4`.
- Loop ends because `list1` is `None`.
- After the loop, `list2` still has `[4]`, so `current.next = list2` attaches `4`.
- Return `dummy.next` -> `1 -> 1 -> 2 -> 3 -> 4 -> 4`.

**Challenges and failed attempts:**
At first, I tried doing this without a `dummy` node by setting `head = list1` or `list2` before the loop, and I forgot to update `current = current.next` inside the `while` loop. Because `current` stayed at the first node, it kept overwriting `current.next` on every iteration and I ended up with a 2-node list instead of all elements. Adding `current = current.next` and using a `dummy` node made the pointer logic much simpler.

# 3. Time Complexity
Time Complexity: O(n + m)

Here `n` is the number of nodes in `list1` and `m` is the number of nodes in `list2`. In the worst case, the `while` loop visits every node from both lists once, and each comparison and pointer update takes `O(1)` time.

# 4. Space Complexity
Space Complexity: O(1)

We reuse the existing nodes from `list1` and `list2` and only allocate one `dummy` node and a pointer variable `current`, so the extra memory is constant.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** In terms of Big-O, `O(n + m)` time and `O(1)` space is already as efficient as possible.
- **What would you need to change?** Another way to write this is recursively (`if list1.val <= list2.val: list1.next = self.mergeTwoLists(list1.next, list2)`), which makes the code shorter.
- **What complexity could the improved solution achieve?** The recursive version still runs in `O(n + m)` time, but uses `O(n + m)` stack space, so the iterative pointer approach is better for memory.
