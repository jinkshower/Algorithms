class Solution:
    def findMin(self, nums: List[int]) -> int:
        # unique and sorted in ascending order
        l, r = 0, len(nums) - 1
        result = 5001
        while (l <= r):
            mid = (l + r) // 2
            # it is in the rotated half 
            result = min(result, nums[mid])
            if nums[l] > nums[r] and nums[mid] >= nums[l]:
                # search right
                l = mid + 1
            else:
                # search left
                r = mid - 1
        
        return result
