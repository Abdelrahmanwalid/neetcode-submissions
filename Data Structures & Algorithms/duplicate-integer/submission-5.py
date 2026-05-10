class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencySet = set()

        for num in nums:
            if num in frequencySet:
                return True
            frequencySet.add(num)
        
        return False
      