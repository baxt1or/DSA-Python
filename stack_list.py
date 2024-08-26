

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        return self.stack.append(data)
    
    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
        return "Stack is empty"
    
    def peek(self):
        
        if len(self.stack) != 0:
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def clear(self):
        return self.stack.clear()
    
    def contains_duplicates(self):
        if len(self.stack) != 0:
            for i in range(len(self.stack)-1):
                if self.stack[i] == self.stack[i+1]:
                   return True
            return False
        else:
            raise IndexError("Empty Stack")

    def is_duplicated(self):
        if len(self.stack) != 0:
            
            for i in range(len(self.stack)):
                for j in range(i+1, len(self.stack)):
                    if self.stack[i] == self.stack[j]:
                        return True
            return False
    
    def is_duplicated_set(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        
        seen = set()

        for item in self.stack:
            if item in seen:
                return True
            seen.add(item)
        return False
    


    def reverse(self):
        if len(self.stack) != 0:
            return self.stack[::-1]
        else:
            raise IndexError("Stack has not be empty")
        
    
    def sum(self):
        if all(isinstance(x,(int, float)) for x in self.stack):
            return sum(self.stack)
        else:
            raise TypeError("String can have sum")
    
    def __str__(self) -> str:
        return str(self.stack)


stack = Stack()

stack.push("Alex")
stack.push("Munisa")
stack.push("Tom")
print(stack.peek())
print(stack.is_empty())
print(stack.size())
print(stack)
print(stack.is_duplicated())
print(stack.reverse())
print(stack.is_duplicated_set())