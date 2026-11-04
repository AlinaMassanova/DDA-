# 1. Problem
Given the `head` of a singly linked list, we need to sort its nodes in ascending order and return the head of the sorted linked list.

# 2. Approach
I used recursive top-down Merge Sort adapted for a linked list:
1. Base case: if `head` is `None` or has only one node (`head.next is None`), it is already sorted, so return `head`.
2. Find the middle of the linked list using `slow` and `fast` pointers, plus a `prev` pointer that stays one step behind `slow`. When `fast` reaches the end, `slow` is at the start of the second half.
3. Cut the list into two separate halves by setting `prev.next = None`. Now `head` is the first half and `slow` is the second half.
4. Recursively sort both halves: `left_side = self.sortList(head)` and `right_side = self.sortList(slow)`.
5. Merge the two sorted halves using a `merge(l1, l2)` helper method with a `dummy` node, connecting the smaller node at each step.

**Tracing with an example:**
Suppose the linked list is `4 -> 2 -> 1 -> 3`:
- Step 1 (Split `4 -> 2 -> 1 -> 3`):
  - `slow` moves to `2`, then `1`; `fast` reaches `None`; `prev` is at `2`.
  - `prev.next = None` cuts the list into `4 -> 2` and `1 -> 3`.
- Step 2 (Sort left half `4 -> 2`):
  - Split `4 -> 2` into `4` and `2` (both hit the single-node base case).
  - `merge(4, 2)` compares `4` and `2` -> returns `2 -> 4`.
- Step 3 (Sort right half `1 -> 3`):
  - Split `1 -> 3` into `1` and `3` (both hit the base case).
  - `merge(1, 3)` compares `1` and `3` -> returns `1 -> 3`.
- Step 4 (Final merge of `2 -> 4` and `1 -> 3`):
  - Iter 1: `2 > 1` -> attach `1` (`l2` moves to `3`).
  - Iter 2: `2 <= 3` -> attach `2` (`l1` moves to `4`).
  - Iter 3: `4 > 3` -> attach `3` (`l2` becomes `None`).
  - Attach remaining `l1` (`4`).
  - Result: `1 -> 2 -> 3 -> 4`.

**Challenges and failed attempts:**
When I first wrote the splitting step with `slow` and `fast`, I forgot to keep a `prev` pointer to set `prev.next = None`. Because I never disconnected the end of the first half from `slow`, calling `self.sortList(head)` kept passing the entire original list forever and crashed with `RecursionError: maximum recursion depth exceeded`. Adding `prev = slow` inside the loop and setting `prev.next = None` right after the loop properly broke the list into two halves.

# 3. Time Complexity
Time Complexity: O(n log n)

Splitting the list with `slow` and `fast` takes `O(n)` steps across each level, and merging the sorted sublists also takes `O(n)` steps per level. Since the list is divided in half at every step, there are `log2(n)` levels of recursion, resulting in `O(n log n)` total time.

# 4. Space Complexity
Space Complexity: O(log n)

Even though we reuse the existing `ListNode` objects instead of creating new ones during merging, the recursive calls `self.sortList(head)` and `self.sortList(slow)` take `O(log n)` frames on the call stack.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** The `O(n log n)` time complexity is optimal, but the `O(log n)` space used by recursion can be improved to `O(1)`.
- **What would you need to change?** To get rid of the recursion stack, we would need to rewrite the algorithm using Bottom-Up Merge Sort: start with `step = 1` and iteratively merge adjacent pairs of size 1, then pairs of size 2, then size 4, and so on until `step >= n`.
- **What complexity could the improved solution achieve?** Bottom-up iterative merge sort runs in `O(n log n)` time and strict `O(1)` extra space.
