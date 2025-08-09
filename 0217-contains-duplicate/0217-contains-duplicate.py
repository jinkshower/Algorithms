class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for i in range(len(nums)):
            if nums[i] in cache:
                return True
            cache.add(nums[i])
        return False