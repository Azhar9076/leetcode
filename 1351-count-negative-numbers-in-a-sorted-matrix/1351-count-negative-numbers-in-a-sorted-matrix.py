class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cols = len(grid[0])
        count = 0

        for row in grid:
            low, high = 0, cols - 1

            while low <= high:
                mid = (low + high) // 2

                if row[mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1

            count += cols - low

        return count