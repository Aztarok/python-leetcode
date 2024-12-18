from typing import Optional


class node:
    def __init__(self, data=None, next = None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            if cur_node.next == None:
                print("ERROR: 'Erase' index out of range!")
                return
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' index out of range!")
            return
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            if cur_node.next == None:
                print("ERROR: 'Erase' index out of range!")
                return
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx += 1

    def evenOdd(self):
        cur_idx = 1
        cur_node = self.head
        evens = []
        odds = []
        while cur_node.next != None:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx % 2 == 0:
                evens.append(cur_node.data)
            else:
                odds.append(cur_node.data)
            cur_idx += 1
        return odds + evens


def main():
    my_list = linked_list()
    my_list.display()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)
    my_list.display()
    print("Element at 1st index:", my_list.get(1))
    my_list.display()
    my_list.display()
    print(my_list.evenOdd())


if __name__ == "__main__":
    main()
