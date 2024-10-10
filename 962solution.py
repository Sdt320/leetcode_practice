class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        self.maxramp=0
        ramp=0
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<=nums[j]:
                    ramp=j-i
                    if ramp > self.maxramp:
                        self.maxramp=ramp
                        
        return self.maxramp


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        
        # Step 1: Build a stack of indices with decreasing values
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Step 2: Traverse from the end to find the widest ramp
        max_ramp = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_ramp = max(max_ramp, j - stack.pop())
        
        return max_ramp
