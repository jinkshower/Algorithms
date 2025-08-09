class Solution:
    def trap(self, height: List[int]) -> int:
        # 
        n = len(height)
        left = [0] * n
        right = [0] * n

        left_max = 0
        for i in range(n):
            if height[i] > left_max:
                left_max = height[i]
            left[i] = left_max
        right_max = 0
        for i in range(n - 1, -1, -1):
            if height[i] > right_max:
                right_max = height[i]
            right[i] = right_max
        
        # [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
        # [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
        res = 0
        for i in range(1, n - 1):
            water = min(left[i], right[i]) - height[i]
            res += water 
        return res