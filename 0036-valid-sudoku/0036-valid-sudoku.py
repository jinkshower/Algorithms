class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # O(n ^2) O(n^2)
        rowSet = {}
        colSet = {}
        squSet = {}

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                    
                rowKey = 'row' + str(i)
                colKey = 'col' + str(j)
                squKey = 'squ' + str((i // 3) * 3 + (j // 3))

                if rowKey in rowSet:
                    if cur in rowSet[rowKey]:
                        return False
                    else:
                        rowSet[rowKey].add(cur)
                else:
                    rowSet[rowKey] = set()
                    rowSet[rowKey].add(cur)
                    
                if colKey in colSet:
                    if cur in colSet[colKey]:
                        return False
                    else:
                        colSet[colKey].add(cur)
                else:
                    colSet[colKey] = set()
                    colSet[colKey].add(cur)
                    
                if squKey in squSet:
                    if cur in squSet[squKey]:
                        return False
                    else:
                        squSet[squKey].add(cur)
                else:
                    squSet[squKey] = set()
                    squSet[squKey].add(cur)
        return True