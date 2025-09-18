class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        
        n = len(s1)

        s2_map = {}
        for i in range(n):
            s2_map[s2[i]] = s2_map.get(s2[i], 0) + 1
        
        if s1_map == s2_map:
            return True

        l = 0

        for r in range(n, len(s2)):
            s2_map[s2[r]] = s2_map.get(s2[r], 0) + 1
            s2_map[s2[l]] -= 1
            if s2_map[s2[l]] == 0:
                del s2_map[s2[l]]

            if s1_map == s2_map:
                return True
            l += 1

        return False