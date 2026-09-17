class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0
        while x > 0:
            d = x % 10
            reverse = reverse * 10 + d
            x //= 10
        return original == reverse    
    

        