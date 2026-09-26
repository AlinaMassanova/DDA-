# 1. Problem
We are given an array of integers that is already sorted in ascending order, and a `target` integer. The goal is to find the index of the `target` in the array. If the target does not exist in the array, we must return `-1`.

# 2. Approach
Because the array is already sorted, we can use the Binary Search algorithm rather than checking every single number one by one. 
I set up two pointers: `left` at the start of the array and `right` at the end. I then find the middle element. 
- If the middle element is the target, I'm done.
- If the middle element is smaller than the target, I know the target must be in the right half of the array, so I move my `left` pointer to `mid + 1`.
- If the middle element is larger than the target, the target must be in the left half, so I move my `right` pointer to `mid - 1`.
I repeat this process until `left` is greater than `right`, which means the target isn't in the array.

# 3. Time Complexity
**Time Complexity: O(log n)**
In the worst-case scenario, the algorithm cuts the search space in half during every step of the while loop. Instead of checking `n` elements, we only check a fraction of them. The number of operations grows logarithmically with the size of the array `n`. 

# 4. Space Complexity
**Space Complexity: O(1)**
The algorithm only uses a few integer variables (`left`, `right`, and `mid`) to keep track of indices. It does not create any new arrays or use memory that scales with the input size. Therefore, the extra space used is constant.

# 5. Reflection / Improvement
A brute-force approach would be a simple linear search using a `for` loop to check every element, which would have an O(n) time complexity. My implemented solution is already optimized to O(log n) using binary search, which is the most efficient way to search a sorted array. No further algorithmic improvements are necessary for this specific problem.