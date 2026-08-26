from collections import Counter
from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return sum(num for num, freq in counts.items() if freq == 1)
        