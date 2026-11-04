# 1. Problem
We are given an array of integers `nums` and need to sort it in ascending order and return it, without using any built-in sorting functions like `sort()` or `sorted()`.

# 2. Approach
I implemented the Merge Sort algorithm using recursion and a `merge` helper function:
1. Base case: if `nums` has `1` or `0` elements, it is already sorted, so return `nums`.
2. Find the middle index `mid = len(nums) // 2` and split the array into two halves: `nums[:mid]` and `nums[mid:]`.
3. Recursively sort both halves with `self.sortArray(...)`.
4. Combine the two sorted halves using `self.merge(left_half, right_half)`:
   - Use two index pointers `i = 0` and `j = 0`.
   - Compare `left[i]` and `right[j]`, append the smaller element to `result`, and move that pointer forward.
   - Once one half runs out of elements, append all remaining elements from the other half to `result`.

**Tracing with an example:**
Suppose `nums = [5, 2, 3, 1]`:
- Split `[5, 2, 3, 1]` at `mid = 2` into `[5, 2]` and `[3, 1]`.
- Sort left half `[5, 2]`:
  - Split at `mid = 1` into `[5]` and `[2]`. Both have length 1 (base case).
  - Merge `[5]` and `[2]`: compare `5` and `2` -> `2` goes first, then remaining `5` -> returns `[2, 5]`.
- Sort right half `[3, 1]`:
  - Split at `mid = 1` into `[3]` and `[1]`. Both hit base case.
  - Merge `[3]` and `[1]`: compare `3` and `1` -> `1` goes first, then remaining `3` -> returns `[1, 3]`.
- Final merge of `[2, 5]` and `[1, 3]`:
  - Iter 1: compare `2` and `1` -> append `1` (`result = [1]`, `j = 1`).
  - Iter 2: compare `2` and `3` -> append `2` (`result = [1, 2]`, `i = 1`).
  - Iter 3: compare `5` and `3` -> append `3` (`result = [1, 2, 3]`, `j = 2`).
  - Right list is finished, so append remaining `5` from left list -> `result = [1, 2, 3, 5]`.

**Challenges and failed attempts:**
First, I tried writing a simple Bubble Sort with two nested `for` loops because it was the easiest to code from scratch. It passed the basic test cases `[5, 2, 3, 1]` and `[5, 1, 1, 2, 0, 0]`, but failed with `Time Limit Exceeded` on large test cases because `O(n^2)` is too slow when `n = 50,000`. Then I tried QuickSort picking the first element `nums[0]` as the pivot, which also timed out on arrays that were already sorted or had many duplicate numbers. Switching to Merge Sort solved the problem because it always splits the array in half regardless of the input values.

# 3. Time Complexity
Time Complexity: O(n log n)

At each level of recursion, we split the array in half, so the recursion tree has `log2(n)` levels. At every level, the `merge` function processes a total of `n` elements in linear `O(n)` time. Multiplying the work per level by the number of levels gives `O(n log n)` in the best, average, and worst cases.

# 4. Space Complexity
Space Complexity: O(n)

In `merge`, we allocate a new `result` list that holds up to `n` elements at the top level, and slicing `nums[:mid]` and `nums[mid:]` also creates temporary sub-arrays. The recursion stack uses `O(log n)` frames, so the overall space complexity is dominated by `O(n)`.

# 5. Reflection / Improvement
- **Is there a more efficient approach?** For comparison-based sorting, `O(n log n)` time is the theoretical lower bound, so time complexity cannot be improved in general. However, memory usage can be reduced.
- **What would you need to change?** Instead of creating new slices `nums[:mid]` and new `result` lists on every recursive call, we could pass index boundaries `(left_idx, right_idx)` and reuse a single temporary array of size `n`, or use Heap Sort to sort the array completely in place.
- **What complexity could the improved solution achieve?** Heap Sort achieves `O(n log n)` time complexity with `O(1)` auxiliary space.
