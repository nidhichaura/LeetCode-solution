class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                val = int(s[i - 2:i])
                res.append(chr(ord('a') + val - 1))
                i -= 3
            else:
                val = int(s[i])
                res.append(chr(ord('a') + val - 1))
                i -= 1
        return "".join(reversed(res))            