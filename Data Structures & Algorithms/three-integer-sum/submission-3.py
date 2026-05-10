class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                numSum = nums[i] + nums[k] + nums[j]
                if numSum > 0:
                    k -= 1
                elif numSum == 0:
                    result.add((nums[i], nums[k],nums[j]))
                    j+=1
                    
                else:
                    j += 1
        return list(result)