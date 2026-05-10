class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        smallest = self.stack[0]
        for n in range(len(self.stack)):
            if self.stack[n] < smallest:
                smallest = self.stack[n]
        return smallest

