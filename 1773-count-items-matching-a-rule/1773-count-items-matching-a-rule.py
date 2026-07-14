class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "type":
            key_index = 0
        elif ruleKey == "color":
            key_index = 1
        else:
            key_index = 2
        return sum(1 for item in items if item[key_index] == ruleValue)         
        