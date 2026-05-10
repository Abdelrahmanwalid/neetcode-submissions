class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        result = []

        for num in nums:
            numMap[num] = numMap.get(num,0) + 1
        
        for i in range(k):
            maxNum = max(numMap, key=numMap.get)
            result.append(maxNum)
            del numMap[maxNum]
        return result