class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # [0]
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    # search right
                    l = m + 1
                else:
                    #search left
                    r = m - 1
            # right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    #search left
                    r = m - 1
                else:
                    #search right
                    l = m + 1
        return -1 
             