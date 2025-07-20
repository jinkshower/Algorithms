class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        dStack = []

        for idx, tem in enumerate(temperatures):
            while dStack and temperatures[dStack[-1]] < tem:
                popped = dStack.pop()
                days = idx - popped
                result[popped] = days
            dStack.append(idx)
        return result