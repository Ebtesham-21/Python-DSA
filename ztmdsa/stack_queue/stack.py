class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def peek(self):
        if not self.is_empty():
            return self.length[-1]
        return None
    