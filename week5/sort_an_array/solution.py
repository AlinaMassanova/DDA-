class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        return self.merge(left_half, right_half)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = 0
        j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                
        while i < len(left):
            result.append(left[i])
            i += 1
            
        while j < len(right):
            result.append(right[j])
            j += 1
            
        return result
