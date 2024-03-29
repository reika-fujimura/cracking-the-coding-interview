class Queue:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return (len(self.items==0))

    def push(self, e):
        self.items.append(e)

    def pop(self):
        if self.items:
            return 
        return self.items.pop(0)

    def peek(self):
        if self.items:
            return
        return self.items[0]

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return bool(self.items)