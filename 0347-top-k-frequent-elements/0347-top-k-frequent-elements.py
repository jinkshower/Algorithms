class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash 
        # heap entry 
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(len(heap)):
            popped = heapq.heappop(heap)
            res.append(popped[1])
        
        return res