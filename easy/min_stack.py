class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min.append(val)
        else:
            self.min.append(min(self.min[-1], val))
        self.stack.append(val)

    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
