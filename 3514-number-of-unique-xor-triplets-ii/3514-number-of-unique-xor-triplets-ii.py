class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        unique_nums = list(set(nums))
        n = len(unique_nums)
        pair_xors = set()
        for i in range(n):
            for j in range(i, n):
                pair_xors.add(unique_nums[i] ^ unique_nums[j])
        triplet_xors = set()
        for x in unique_nums:
            for p in pair_xors:
                triplet_xors.add(x ^ p)
        return len(triplet_xors)                