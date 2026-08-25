from collections import Counter
from typing import List
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        def sort_key(x):
            return (count[x], -x)
        return sorted(nums, key=sort_key)    
