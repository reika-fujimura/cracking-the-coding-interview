from stack import Stack

class MinStack(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.minval = Stack()

    def push(self, e):
        super().push(e)
        if not self.minval or self.minval.peek() > e:
            self.minval.push(e)
        
    def pop(self):
        val = super.pop()
        if self.minval.peek() == val:
            self.minval.pop()
        return val

    def minivalue(self):
        return self.minval.peek()