class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        stack = []   
        ans = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                d[nums2[i]] = stack[-1]
            else:
                d[nums2[i]] = -1
            stack.append(nums2[i])
        for y in nums1:
            if y in d:
                ans.append(d[y])
        return ans                    

