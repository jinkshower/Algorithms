class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]
        m, n = len(grid), len(grid[0])

        freshCount = 0
        rotten = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        q = collections.deque(rotten)
        level = 0

        if freshCount == 0:
            return 0

        while q:
            if freshCount == 0:
                return level

            qlen = len(q)
            for _ in range(qlen):
                cx , cy = q.popleft()

                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]

                    if nx < 0 or nx == m or ny < 0 or ny == n:
                        continue
                    if grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        freshCount -= 1
                        q.append((nx, ny))
            if q:
                level += 1
        return -1 
                    
