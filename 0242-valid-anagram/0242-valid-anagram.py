class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n + m) / O(1)
        alpha = [0] * 26
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            alpha[idx] += 1
        
        for i in range(len(t)):
            idx = ord(t[i]) - ord('a')
            alpha[idx] -= 1
        
        for i in range(len(alpha)):
            if alpha[i] != 0:
                return False
        return True