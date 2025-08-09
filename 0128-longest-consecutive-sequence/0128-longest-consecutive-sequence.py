class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #  1 , 2, 3, 4, 100 ,200 
        # 1, 1, 2, 2, 4, 6, 7, 8, 100, 101 n logn for sorting / O(n)
        
        # hash set
        # 0 99 100 3 5 7 2 8 4 6 1
        # [c] [c] [c][cccccccccccccc]

        cache = set(nums)
        maxLen = 0
        for num in cache:
            # not start
            if num - 1 in cache:
                continue
            cur = num
            curLen = 0
        
            while cur in cache:
                curLen += 1
                cur += 1
            
            maxLen = max(maxLen, curLen)
        
        return maxLen
