class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        result = 0

        while left < right:
            gap = right - left
            smallest = 0

            if heights[left] > heights[right]:
               smallest = heights[right]
            else:
                smallest = heights[left]
            if smallest * gap > result:
                result = smallest * gap
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
            
        return result