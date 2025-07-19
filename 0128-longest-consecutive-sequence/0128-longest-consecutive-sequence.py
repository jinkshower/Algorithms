class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = set()
        for num in nums:
            count.add(num)
        
        max_length = 1
        for num in count:
            cur = num
            length = 0
            if cur - 1 in count:
                continue

            while cur in count:
                cur += 1
                length += 1
            
            max_length = max(max_length , length)
        
        return max_length

        # numSet = set(nums)
        # longest = 0

        # for n in nums:
        #     if (n - 1) not in numSet:
        #         length = 0
        #         while (n + length) in numSet:
        #             length += 1
        #         longest = max(longest, length)
        # return longest 