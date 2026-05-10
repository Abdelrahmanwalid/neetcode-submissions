class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        left = 0
        right = len(numbers) -1

        while left < right:
            if numbers[right] > (target - numbers[left]):
                right -= 1
            elif numbers[left] <  (target - numbers[right]):
                left += 1
            elif numbers[left] + numbers[right] == target:
                return [left+1,right+1]
        return []