class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cache = set()

        l = r = 0
        n = len(s)
        result = 0

        while r < n:
            while s[r] in cache:
                cache.remove(s[l])
                l += 1
            cache.add(s[r])
            result = max(result, r - l + 1)
            r += 1
        return result
