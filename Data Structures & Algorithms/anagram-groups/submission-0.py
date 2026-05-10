class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedArray = []
        wordMap = {}
        result = []
        for word in strs:
            sortedString = ''.join(sorted(word))
            if sortedString in wordMap:
                wordMap[sortedString].append(word)
            else:
                wordMap[sortedString] = [word]
        for key in wordMap:
            result.append(wordMap[key])
        return result
        

            
        