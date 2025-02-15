from typing import List
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return min(self.stack)
        
def main() -> None:
    minStack = MinStack()
    minStack.push(1)
    minStack.push(2)
    minStack.push(0)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
    
if __name__ == "__main__":
    main()