class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0

        for num in nums:
            count += 1
            if num == 0:
                count = 0
            maxCount = max(maxCount, count)
        return maxCount