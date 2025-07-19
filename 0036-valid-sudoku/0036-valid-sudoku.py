class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1-5
        # 1-3
        hashMap = {}

        # row num digit
        # col num digit
        # square num digit 
        # if already in the map -> False

        def findSquare(row, col):
            return (row // 3) * 3 + (col // 3)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                rowKey = "R" + str(i) + board[i][j]
                colKey = "C" + str(j) + board[i][j]
                squKey = "S" + str(findSquare(i, j)) + str(board[i][j])

                if rowKey in hashMap or colKey in hashMap or squKey in hashMap:
                    return False
                hashMap[rowKey] = 1
                hashMap[colKey] = 1
                hashMap[squKey] = 1
        
        return True