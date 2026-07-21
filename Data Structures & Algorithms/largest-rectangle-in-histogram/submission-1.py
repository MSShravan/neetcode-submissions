class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                sI, sH = stack.pop()
                maxArea = max(maxArea, sH * (i-sI))
                start = sI
            stack.append((start, h))
        
        
        for i,h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
