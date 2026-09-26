# 1. Problem
We have `n` versions of a product [1, 2, ..., n] and we want to find out which one was the first bad version. The catch is that once a version goes bad, every version after it is also bad. We are given an API `isBadVersion(version)` that returns a boolean indicating whether a version is bad. We need to find the first bad version using the fewest API calls possible.

# 2. Approach
This problem can be thought of as finding the first `True` in a sorted array of booleans (e.g., `[False, False, True, True, True]`). I used a modified binary search to solve this. 
I set `left` to 1 and `right` to `n`. I check the `mid` version using the API.
- If `isBadVersion(mid)` is true, `mid` could be the first bad version, or the first bad one is to the left of it. So, I update `right = mid` (keeping `mid` in the search space).
- If `isBadVersion(mid)` is false, all versions up to `mid` are good. The first bad version must be strictly to the right, so I update `left = mid + 1`.
The loop stops when `left` equals `right`, which points exactly to the first bad version.

# 3. Time Complexity
**Time Complexity: O(log n)**
Just like standard binary search, the search space is divided by two with each iteration. Therefore, the number of calls made to the `isBadVersion` API scales logarithmically with `n`.

# 4. Space Complexity
**Space Complexity: O(1)**
The algorithm only initializes a few pointers (`left`, `right`, and `mid`). It doesn't store any arrays or history of the versions checked, meaning it uses a constant amount of extra memory regardless of how large `n` is.

# 5. Reflection / Improvement
The brute-force solution would be to call `isBadVersion(i)` starting from 1 up to `n` in a `for` loop until we hit the first `True`. That would result in a Time Complexity of O(n), which would time out for large values of `n`. The binary search approach I implemented improves this to O(log n), which is the most efficient time complexity possible for this problem.