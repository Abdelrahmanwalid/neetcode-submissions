class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res= []
        subset = []
        
        def backTrack (num):
            if num >= len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[num])
            backTrack(num + 1)

            subset.pop()
            backTrack(num+1)

            backTrack
        backTrack(0)

        return res
