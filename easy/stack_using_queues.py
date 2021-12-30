from collections import deque

class MyStack:

    def __init__(self):
        self.stack = deque()
        self.len = 0

    def push(self, x: int) -> None:
        self.stack.appendleft(x)
        self.len += 1

    def pop(self) -> int:
        temp_len = self.len
        while temp_len != 0:
            last = self.stack.pop()
            if temp_len != 1:
                self.stack.appendleft(last)
            temp_len -= 1
        self.len -= 1
        return last

    def top(self) -> int:
        item = self.pop()
        self.push(item)
        return item

    def empty(self) -> bool:
        return self.len == 0



myStack = MyStack()
myStack.push(1)
myStack.push(2)
a = myStack.top() # return 2
b = myStack.pop() # return 2
c = myStack.empty() # return False
pass