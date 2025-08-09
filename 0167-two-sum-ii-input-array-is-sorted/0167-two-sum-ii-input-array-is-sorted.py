class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non -decreasing order sorted
        # 1 2 3 4 5 6    target 10
        n = len(numbers)
        l, r = 0, n - 1

        while l < r:
            cur = numbers[l] + numbers[r]

            if cur == target:
                return [l + 1, r + 1]
            elif cur > target:
                r -= 1
            elif cur < target:
                l += 1
        