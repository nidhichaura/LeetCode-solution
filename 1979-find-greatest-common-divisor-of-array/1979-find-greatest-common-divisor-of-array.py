
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maximum_num = max(nums)
        minimum_num = min(nums)
        a, b = minimum_num, maximum_num
        while b>0:
            a, b = b, a % b
        return a    

        