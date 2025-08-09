class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(m * n) O(m)
        # hash map  key - serialized arrays : string, string .. 

        cache = {}
        
        def hashArray(arr):
            res = ''
            for i in range(len(arr)):
                res += str(i) + ":" + str(arr[i]) + ","
            return res

        for i in range(len(strs)):
            alpha = [0] * 26
            cur = strs[i]
            for j in range(len(cur)):
                alpha[ord(cur[j]) - ord('a')] += 1
            key = hashArray(alpha)

            if key in cache:
                cache[key].append(cur)
            else:
                cache[key] = [cur]
        
        return list(cache.values())
