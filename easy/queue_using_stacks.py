class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            item = self.stack.pop()
            if len(self.stack) != 0:
                self.stack_2.append(item)
        while self.stack_2:
            self.push(self.stack_2.pop())
        return item

    def peek(self) -> int:
        while self.stack:
            item = self.stack.pop()
            self.stack_2.append(item)
        while self.stack_2:
            self.push(self.stack_2.pop())
        return item



    def empty(self) -> bool:
        return not len(self.stack)


myQueue = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
a = myQueue.peek() # return 1
b = myQueue.pop() # return 1, queue is [2]
c = myQueue.empty() # return false
pass
