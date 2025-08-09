class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] + [0]*n + [1]
        suffix = [1] + [0]*n + [1]

        for i in range(n):
            prefix[i + 1] = prefix[i] * nums[i]
        
        for i in range(n - 1, -1, -1):
            suffix[i + 1] = suffix[i + 2] * nums[i]
        
        res = []
        for i in range(n):
            product = prefix[i] * suffix[i + 2]
            res.append(product)
        
        return res