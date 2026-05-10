class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in range(len(nums)):
            pointer = 0
            current = 1
            for j in range(len(nums)):
                if j != i:
                    current *= nums[j]
            result.append(current)
        return result


    