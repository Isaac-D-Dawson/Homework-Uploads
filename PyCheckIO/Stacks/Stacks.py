class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    @property
    def pop(self):
        if not self.is_empty:
            return self.stack.pop()
    
    @property
    def peek(self):
        if not self.is_empty:
            return self.stack[-1]
    
    @property
    def is_empty(self):
        return not len(self.stack) #> 0
    
    @property
    def display(self):
        return self.stack
