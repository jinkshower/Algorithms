class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each string, hash map it
        hash_map = {}

        def make_key(s):
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            return tuple(count)

        for s in strs:

            made = make_key(s)
            
            if made in hash_map:
                hash_map[made].append(s)
            else:
                hash_map[made] = [s]
        
        return list(hash_map.values())