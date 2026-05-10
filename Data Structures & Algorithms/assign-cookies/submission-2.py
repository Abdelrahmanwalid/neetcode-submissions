class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()  # in-place
        s.sort()
        right = 0
        content = 0
        left = 0
        while left < len(g) and right < len(s):
                while  right < len(s) and g[left] > s[right] :
                        right += 1
                if right < len(s) and g[left] <= s[right]:
                        content += 1
                right += 1
                left += 1
        return content