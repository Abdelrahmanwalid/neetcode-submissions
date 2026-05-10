class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in reversed(s):
            if count == 0 and char == ' ':
                continue
            if char != ' ':
                count += 1
            if char == ' ':
                return count
        return 1