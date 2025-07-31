class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        tmp = set()
        l, r = 0, 0
        max_len = 0

        while r < len(s):
            while s[r] in tmp:
                tmp.remove(s[l])
                l += 1
            tmp.add(s[r])
            max_len = max(max_len , r - l + 1)
            r += 1
        
        return max_len