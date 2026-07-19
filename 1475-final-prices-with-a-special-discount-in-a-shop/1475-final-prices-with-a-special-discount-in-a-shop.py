class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = list(prices)
        stack = []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                idx = stack.pop()
                answer[idx] -= price  
             
            stack.append(i)
            
        return answer