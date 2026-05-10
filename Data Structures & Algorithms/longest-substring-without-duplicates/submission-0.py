class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right= 0
        freqSet = set()
        answer= 0

        for right in range(len(s)):
            
            while s[right] in freqSet:
                 freqSet.remove(s[left])
                 left += 1
               
            freqSet.add(s[right])
            longest = (right - left) + 1
            answer = max(answer, longest)
            right += 1
        return answer
