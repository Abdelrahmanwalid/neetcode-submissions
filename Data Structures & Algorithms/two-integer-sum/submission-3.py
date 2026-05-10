class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       numMap = {}

       for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in numMap:
            return [numMap[compliment], i]
        numMap[nums[i]] = i
    