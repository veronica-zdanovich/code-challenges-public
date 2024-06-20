class MinStack:

    def __init__(self):
        self.stack = list()
        self.min_stack = list()
        self.min_item = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_stack) == 0:
            self.min_item = val
            self.min_stack.append(val)
        else:
            self.min_item = min(self.min_stack[-1], val)
            self.min_stack.append(self.min_item)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
