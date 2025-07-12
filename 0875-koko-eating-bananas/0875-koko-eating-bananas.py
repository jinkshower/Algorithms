class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(k):
            total_time = 0
            for pile in piles:
                total_time += ceil(pile / k)
            return total_time <= h

        start , end = 1, max(piles)
        res = -1

        while start <= end:
            mid = (start + end) // 2
            if canEat(mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res
                