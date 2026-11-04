class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        sum_ = 0
        prod = 1
        while temp > 0:
            r = temp % 10 
            temp //= 10
            sum_ += r
            prod *= r
        return prod - sum_    
         
