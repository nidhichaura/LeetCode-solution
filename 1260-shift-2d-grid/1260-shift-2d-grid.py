class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid), len(grid[0])
        flat = []
        for row in grid:
            flat.extend(row)
        total_elements = len(flat)
        k = k % total_elements
        if k > 0:
            flat = flat[-k:] + flat[:-k]
        result = []
        for i in range(0, total_elements, n):
            result.append(flat[i : i + n]) 
        return result    

