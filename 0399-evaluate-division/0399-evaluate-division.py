class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        n = len(equations)
        graph = collections.defaultdict(list)
        for i in range(n):
            fromN , toN = equations[i]
            weight = values[i]
            graph[fromN].append((toN, weight))
            graph[toN].append((fromN, 1 / weight))

        def dfs(node, end, visited, sum):
            if node == end:
                return sum
            visited.add(node)
             
            for neighbor, weight in graph[node]:
                if neighbor in visited:
                    continue
                result = dfs(neighbor, end, visited, sum * weight)
                if result != -1:
                    return result
            return -1

        result = []
        for query in queries:
            start , end = query
            if start not in graph or end not in graph:
                result.append(-1.0)
            else:
                visited = set()
                result.append(dfs(start, end, visited, 1.0))
        return result
