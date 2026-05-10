class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        currentMax = 0
        while left < right:
            calc = min(heights[left], heights[right]) * (right - left)
            currentMax = max(currentMax, calc)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return currentMax