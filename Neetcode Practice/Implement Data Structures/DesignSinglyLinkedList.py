from typing import List

class node:
    def __init__(self, data: int, next = None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        node_index = 0
        node_current = self.head
        while True:
            if node_current is None:
                return -1
            if node_index == index:
                return node_current.data
            node_current = node_current.next
            node_index += 1

    def insertHead(self, val: int) -> None:
        new_node = node(val)
        new_node.next = self.head
        self.head = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = node(val)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def remove(self, index: int) -> bool:
        print(index)
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                return True
        current_node = self.head
        node_index = 0
        while current_node is not None and current_node.next is not None:
            last_node = current_node
            current_node = current_node.next
            if node_index == index - 1:
                last_node.next = current_node.next
                return True
            node_index += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        current_node = self.head
        while current_node is not None:
            values.append(current_node.data)
            current_node = current_node.next
        return values
def main() -> None:
    testing = LinkedList()
    # print(testing.get(0))
    # print(testing.insertHead(1))
    # print(testing.insertTail(2))
    # print(testing.insertHead(0))
    # print(testing.getValues())
    # print(testing.remove(1))
    # print(testing.getValues())
    
    print(testing.insertTail(1))
    print(testing.insertTail(2))
    print(testing.getValues())
    print(testing.get(1))
    print(testing.remove(1))
    print(testing.insertTail(2))
    print(testing.get(1))
    print(testing.get(0))

if __name__ == "__main__":
    main()