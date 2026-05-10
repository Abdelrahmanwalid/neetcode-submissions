class Solution:
    def isPalindrome(self, s: str) -> bool:
        useful_input = ''.join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(useful_input)-1

        while left < right:
            if useful_input[left] != useful_input[right]:
                return False
            left += 1
            right -= 1
        return True