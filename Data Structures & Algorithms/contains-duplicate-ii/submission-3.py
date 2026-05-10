class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        numMap = {}
        left = 0
        if k == 0:
            return False
        for right in range(len(nums)):
            if right - left > k:
                numMap[nums[left]] -= 1
                if numMap[nums[left]] == 0:
                    del numMap[nums[left]]
                left += 1
    
            if nums[right] in numMap:
                return True

            numMap[nums[right]] = numMap.get(nums[right], 0) + 1
        return False

             

