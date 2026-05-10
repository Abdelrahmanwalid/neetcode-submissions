class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            # Pop all temperatures less than or equal to current
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            # If stack is not empty, calculate the difference in days
            if stack:
                result[i] = stack[-1] - i

            stack.append(i)  # Push index, not temperature
        return result