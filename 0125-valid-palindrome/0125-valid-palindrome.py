class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def parse(str):
            res = ''
            for c in str:
                if c.isalnum():
                    res += c.lower()
            return res

        parsed = parse(s)

        n = len(parsed)
        l, r = 0, n - 1

        while l < r:
            if parsed[l] != parsed[r]:
                return False
            l += 1
            r -= 1

        return True