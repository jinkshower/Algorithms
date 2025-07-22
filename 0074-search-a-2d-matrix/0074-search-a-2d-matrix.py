class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        rowStart, rowEnd = 0, m - 1
        found = -1

        while rowStart < rowEnd:
            mid = (rowStart + rowEnd) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][n - 1]:
                found = mid
                break
            elif matrix[mid][0] > target:
                rowEnd = mid - 1
            elif matrix[mid][0] < target:
                rowStart = mid + 1
        
        if found == -1:
            found = rowStart

        colStart, colEnd = 0, n - 1

        while colStart <= colEnd:
            mid = (colStart + colEnd) //2

            if matrix[found][mid] > target:
                colEnd = mid - 1
            elif matrix[found][mid] < target:
                colStart = mid + 1
            else:
                return True
        return False