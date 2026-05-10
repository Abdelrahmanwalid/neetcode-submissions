class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numMap = set(nums) #O(N) O(N)
        maxCount = 0

        for num in nums:
            count = 1
            number = num
            
            while number - 1 in numMap:
                number = number - 1
                if number in numMap:
                    count += 1
                else:
                    break
            maxCount = max(maxCount, count)
        return maxCount

