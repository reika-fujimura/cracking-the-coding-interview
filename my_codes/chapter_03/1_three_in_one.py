class MultiStack:
    def __init__(self, num_stack, subarray_length) -> None:
        self.array = [0] * (num_stack * subarray_length)
        self.stack_length = [0] * num_stack
        self.subarray_length = subarray_length

    def push(self, stack_no, el):
        self.is_full(stack_no)
        idx = self.stack_length[stack_no] 
        self.array[idx] = el
        self.stack_length[stack_no] += 1

    def pop(self, stack_no):
        self.is_empty(stack_no)
        idx = self.stack_length[stack_no] - 1
        el = self.array[idx]
        self.array[idx] = 0
        self.stack_length[stack_no] -= 1
        return el
    
    def peek(self, stack_no, el):
        self.is_empty(stack_no)
        idx = self.stack_length[stack_no] - 1
        return self.array[idx]

    def is_empty(self, stack_no):
        if self.stack_length[stack_no]==0:
            raise StackIsEmptyError("Stack {} is empty".format(stack_no))

    def is_full(self, stack_no):
        if self.stack_length[stack_no]==self.subarray_length:
            raise StackIsFullError("Stack {} is full".format(stack_no))


class StackError(Exception):
    '''Stack Error'''

class StackIsEmptyError(StackError):
    '''Stack is empty'''

class StackIsFullError(StackError):
    '''Stack is full'''