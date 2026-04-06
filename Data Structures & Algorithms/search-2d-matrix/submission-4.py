def bin_search_int(row: List[int], target):
    l = 0
    r = len(row) - 1
    while (l <= r):
        mid = (l + r) // 2
        if (row[mid] == target):
            return True
        if (target > row[mid]):
            l = mid + 1
        else:
            r = mid - 1
    return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search_row = matrix[0]
        for row in matrix:
            if (row[-1] >= target):
                break

        return bin_search_int(row, target)