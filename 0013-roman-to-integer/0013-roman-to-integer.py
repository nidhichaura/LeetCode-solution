class Solution:
    def value(self, c: str) -> int:
        if c == "I":
            return 1
        if c == "V":
            return 5
        if c == "X":
            return 10
        if c == "L":
            return 50
        if c == "C":
            return 100
        if c == "D":
            return 500
        if c == "M":
            return 1000
        return 0                             
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if i+1 < len(s) and self.value(s[i]) < self.value(s[i+1]):
                result -= self.value(s[i])
            else:
                result += self.value(s[i])
        return result            
       