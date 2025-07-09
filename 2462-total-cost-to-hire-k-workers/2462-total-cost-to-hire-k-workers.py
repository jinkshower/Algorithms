class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        pairs = [(cost, i) for i, cost in enumerate(costs)]
        n = len(costs)
        
        cost_sum = 0
        min_heap = []
        q = deque()
        
        left = candidates
        right = n - candidates
        need = 2 * candidates
        
        if need >= n:
            min_heap = pairs[:]
            heapq.heapify(min_heap)
        else:
            for i in range(left):
                heapq.heappush(min_heap, pairs[i])
            for i in range(left, right):
                q.append(pairs[i])
            for i in range(right, n):
                heapq.heappush(min_heap, pairs[i])
        
        for _ in range(k):
            val, idx = heapq.heappop(min_heap)
            cost_sum += val
            
            if q:
                if idx >= right:
                    pop_val, pop_idx = q.pop()
                    right -= 1
                    heapq.heappush(min_heap, (pop_val, pop_idx))
                else:
                    pop_val, pop_idx = q.popleft()
                    left += 1
                    heapq.heappush(min_heap, (pop_val, pop_idx))
        
        return cost_sum