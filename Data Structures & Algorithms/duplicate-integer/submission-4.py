class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencySet = set()

        for num in nums:
            frequencySet.add(num)
        
        return True if len(frequencySet) != len(nums) else False
      