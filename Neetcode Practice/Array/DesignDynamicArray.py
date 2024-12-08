class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise IndexError("Array is Empty")
        value = self.arr[self.size - 1]
        self.size -= 1
        return value

    def resize(self) -> None:
        self.arr = self.arr + [0] * self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

def main() -> None:
    testing = DynamicArray(5)
    testing.set(0, 1)
    testing.set(1, 2)
    testing.set(2, 3)
    testing.set(3, 4)
    testing.set(4, 5)
    print(testing.getSize())

if __name__ == "__main__":
    main()