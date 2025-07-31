class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}

        n = len(s1)
        m = len(s2)
        if n > m:
            return False

        for i in range(n):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            count2[s2[i]] = 1 + count2.get(s2[i], 0)
        
        if count1 == count2:
            return True

        l = 0
        for r in range(n, m):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)

            count2[s2[l]] -= 1
            if count2[s2[l]] == 0:
                count2.pop(s2[l])
            l += 1

            print(count1)
            print(count2)
            if count1 == count2:
                return True
        
        return False