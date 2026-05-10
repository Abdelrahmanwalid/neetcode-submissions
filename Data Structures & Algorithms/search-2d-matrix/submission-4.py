class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        absoluteRight = len(matrix[0]) - 1


        while row < len(matrix):
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                middle = left + (right - left) // 2
                if matrix[row][absoluteRight] < target:
                    break
                if matrix[row][middle] < target:
                    left = middle + 1
                    
                elif matrix[row][middle] > target:
                    right = middle - 1
                elif matrix[row][middle] == target:
                    return True
                

            row += 1    
        return False


        