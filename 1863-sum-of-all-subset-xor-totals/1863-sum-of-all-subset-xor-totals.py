class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index: int, current_xor: int) -> int:
            if index == len(nums):
                return current_xor
            with_element = dfs(index + 1, current_xor ^ nums[index])
            without_element = dfs(index + 1, current_xor)
            return with_element + without_element
        return dfs(0, 0)    

        