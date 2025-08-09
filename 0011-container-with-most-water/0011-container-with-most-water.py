class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        n = len(height)

        l, r = 0, n - 1
        while l < r:
            h = min(height[l], height[r])
            w = r - l

            maxArea = max(maxArea, h * w)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return maxArea