class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash 
        # heap entry 
        # count = {}

        # for num in nums:
        #     count[num] = count.get(num, 0) + 1
        
        # heap = []
        # for key, val in count.items():
        #     heapq.heappush(heap, (val, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(len(heap)):
        #     popped = heapq.heappop(heap)
        #     res.append(popped[1])
        
        # return res

        # O(n) O(n)
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # len 만큼의 리스트 안의 리스트

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                