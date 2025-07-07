class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        distance = [[-1] * n for _ in range(m)]
        x, y = entrance
        distance[x][y] = 0

        q = deque()
        q.append((x, y))

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if 0 <= nx < m and 0 <= ny < n:
                    if maze[nx][ny] == '.' and distance[nx][ny] == -1:
                        distance[nx][ny] = distance[cx][cy] + 1
                        # 출구 조건: 가장자리이며 entrance는 아님
                        if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                            return distance[nx][ny]
                        q.append((nx, ny))
        
        return -1