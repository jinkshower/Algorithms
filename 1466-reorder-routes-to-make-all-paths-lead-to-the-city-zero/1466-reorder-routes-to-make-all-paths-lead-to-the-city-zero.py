class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # start 0 recur check its neighbors
        # count outgoing routes

        edges = { (a , b) for a, b in connections}
        neighbors = { city : [] for city in range(n)} 
        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)
        visit.add(0)
        dfs(0)
        return changes