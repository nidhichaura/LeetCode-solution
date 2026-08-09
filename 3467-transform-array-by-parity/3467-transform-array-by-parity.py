class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even_count = sum(1 for x in nums if x % 2 == 0)
        odd_count = len(nums) - even_count
        return [0] * even_count + [1] * odd_count