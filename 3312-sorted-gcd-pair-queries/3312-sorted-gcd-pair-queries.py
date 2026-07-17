from typing import List
import bisect
class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)

        counts = [0] * (max_val + 1)
        for num in nums:
            counts[num] += 1

        multiples = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            for j in range(i, max_val + 1, i):
                multiples[i] += counts[j]
        gcd_counts = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
           
            total_pairs = (multiples[i] * (multiples[i] - 1)) // 2
            
            
            sub_pairs = 0
            for j in range(2 * i, max_val + 1, i):
                sub_pairs += gcd_counts[j]
                
            gcd_counts[i] = total_pairs - sub_pairs
            
        
        prefix_sums = []
        gcd_values = []
        current_sum = 0
        
        for i in range(1, max_val + 1):
            if gcd_counts[i] > 0:
                current_sum += gcd_counts[i]
                prefix_sums.append(current_sum)
                gcd_values.append(i)
                
       
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(gcd_values[idx])
            
        return ans        
