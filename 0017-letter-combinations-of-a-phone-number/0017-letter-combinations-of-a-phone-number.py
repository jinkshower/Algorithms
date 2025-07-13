class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # any order -> don't need to care about sorting
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        result = []
        perm = [""] * len(digits)
        n = len(digits)

        def dfs(idx): 
            # if we reached end of perm len which is 2
            # append it to result.
            if idx == n:
                result.append(''.join(perm))
                return
            # for every phone[digits[idx]]
            nums = phone[digits[idx]] # ["a", "b", "c"]
            for i in range(len(nums)):
                perm[idx] = nums[i]
                dfs(idx + 1)

        dfs(0)
        return result
