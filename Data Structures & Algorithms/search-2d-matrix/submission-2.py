class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        topR, botR = 0, ROWS - 1
        while topR <= botR:
            r = (topR + botR)//2
            if target > matrix[r][-1]:
                topR = r + 1
            elif target < matrix[r][0]:
                botR = r - 1
            else:
                break
        
        if topR > botR:
            return False
        
        row = (topR + botR)//2

        l, r = 0, COLS - 1
        while l <= r:
            mid = (l + r)//2
            if target > matrix[row][mid]:
                l = mid+1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False
