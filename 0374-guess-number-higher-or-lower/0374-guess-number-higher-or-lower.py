# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        start = 1
        end = n

        while start <= end:
            middle = (start + end) // 2
            result = guess(middle)

            if result == 0:
                return middle
            elif result == -1:
                end = middle - 1
            else:
                start = middle + 1
        return middle