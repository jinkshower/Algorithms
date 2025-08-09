class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        found = set()
        for i in range(n):
            
            l , r = i + 1, n - 1
            while l < r:
                cur = nums[i] + nums[l] + nums[r]
                if cur == 0:
                    found.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    r -= 1
            
        return list(found)