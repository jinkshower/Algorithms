class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        
        for idx, num in enumerate(nums):
            l, r =  idx + 1, n - 1

            while l < r:
                curSum = num + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    result.add((num , nums[l], nums[r]))
                    l , r = l + 1, r - 1
        
        return list(result)

