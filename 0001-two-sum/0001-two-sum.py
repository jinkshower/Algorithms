class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) , O(n)
        cache = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in cache:
                return [i, cache[find]]
            cache[nums[i]] = i
        return None
        