class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (i < j < k) and (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        count += 1
        return count                