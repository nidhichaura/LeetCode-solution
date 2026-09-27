class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_ = s.strip()
        return len(s_.split(' ')[-1])

        