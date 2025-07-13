class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # if k >= n early return 
        # if sum already larger than n don't search that road
        # if path contains to search road, skip it

        if k >= n:
            return []
        result = []
        path = []

        def dfs(start, idx, sum):
            nonlocal path
            if sum > n:
                return
            
            if idx == k and sum == n:
                result.append(path[:])
                return
            
            for i in range(start, 10):
                path.append(i)
                dfs(i + 1 ,idx + 1, sum + i)
                path.pop()

        dfs(1, 0, 0)
        return result
